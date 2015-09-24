# coding=utf-8

import logging
import os
import subprocess
import datetime

from django.core.management.base import BaseCommand
from django.conf import settings

from html5helper.utils import wrapper_raven
from clawer.models import ClawerTaskGenerator, Clawer, ClawerTask
from clawer.utils import Download, UrlCache
import traceback


def run(task_generator_id):
    logging.info("run task generator %d" % task_generator_id)
    
    task_generator = ClawerTaskGenerator.objects.get(id=task_generator_id)
    if not (task_generator.status==ClawerTaskGenerator.STATUS_ON and task_generator.clawer.status==Clawer.STATUS_ON):
        return False
    
    path = task_generator.product_path()
    task_generator.write_code(path)
    
    p = subprocess.Popen([settings.PYTHON, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  #("%s %s" % (settings.PYTHON, path), "r")
    for line in p.stdout:
        js = ClawerTaskGenerator.parse_line(line)
        if not js:
            logging.warning("unknown line: %s" % line)
            continue
        
        try:
            url_cache = UrlCache(js['uri'])
            if url_cache.has_url():
                raise Exception("%s has exists", js['uri'])
            url_cache.add_it()
            
            ClawerTask.objects.create(clawer=task_generator.clawer, task_generator=task_generator, uri=js["uri"],
                                  cookie=js.get("cookie"), 
                                  download_engine=js.get("download_engine") if "download_engine" in js else Download.ENGINE_PHANTOMJS)
        except:
            logging.error("add %s failed: %s", js['uri'], traceback.format_exc(10))
        
    err = p.stderr.read()
    
    status = p.wait()
    if status != 0:
        logging.error("run task generator %d failed: %s" % (task_generator.id, err))
        return False
    
    return True
 
                

class Command(BaseCommand):
    args = "task_generator_id"
    help = "Run task generator"
    
    @wrapper_raven
    def handle(self, *args, **options):
        task_generator_id = int(args[0])
        run(task_generator_id)