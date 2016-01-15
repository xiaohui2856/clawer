# -*- coding: utf-8 -*-

from django.db import models
import profiles.settings as settings


class Base(object):
    """数据库操作基本类
    """

    def update(self, model, data):
        """if is exist update else insert
        """

        type_date = settings.type_date
        type_float = settings.type_float

        query = model.objects.filter(enter_name=data['enter_name'])
        if (len(query) == 0):
            fields = self._meta.get_all_field_names()
            for field in fields:
                value = data.get(field)
                if value is None:
                    pass
                elif field in type_date:
                    pass
                elif field in type_float:
                    pass
                elif field in data:
                    setattr(self, field, value)
                else:
                    pass
            self.save()
        else:
            fields = query[0]._meta.get_all_field_names()
            for field in fields:
                print field
                value = data.get(field)
                if value is None:
                    pass
                elif field in type_date:
                    pass
                elif field in type_float:
                    pass
                elif field in data:
                    print "%s : %s" % (field, value)
                    setattr(query[0], field, value)
                else:
                    pass
            query[0].save()


class Basic(models.Model, Base):
    """公司基本类
    """

    credit_code = models.CharField(max_length=20, null=True, blank=True)
    enter_name = models.CharField(max_length=50, null=True, blank=True)
    enter_type = models.CharField(max_length=20, null=True, blank=True)
    corporation = models.CharField(max_length=30, null=True, blank=True)
    register_capital = models.FloatField(null=True)
    establish_date = models.DateTimeField(null=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)
    business_scope = models.TextField(null=True)
    register_gov = models.CharField(max_length=50, null=True, blank=True)
    check_date = models.DateTimeField(null=True)
    register_status = models.CharField(max_length=20, null=True, blank=True)
    register_num = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = "basic"


class IndustryCommerceAdministrativePenalty(models.Model, Base):
    """工商-行政处罚
    """

    penalty_decision_num = models.IntegerField()
    illegal_type = models.CharField(max_length=30)
    penalty_content = models.CharField(max_length=50)
    penalty_decision_gov = models.CharField(max_length=50)
    penalty_decision_date = models.DateTimeField()
    detail = models.CharField(max_length=30)
    penalty_register_date = models.DateTimeField()
    enter_name = models.CharField(max_length=50)
    creidit_code = models.CharField(max_length=20)
    corporation = models.CharField(max_length=30)
    penalty_publicity_time = models.DateTimeField()
    enter_id = models.CharField(max_length=30)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industrycommerce_administrative_penalty"


class IndustryCommerceBranch(models.Model, Base):
    """工商-分支机构
    """

    enter_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=30)
    register_gov = models.CharField(max_length=50)
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_branch"


class IndustryCommerceChange(models.Model, Base):
    """工商-变更
    """

    modify_item = models.CharField(max_length=30)
    modify_before = models.CharField(max_length=50)
    modify_after = models.CharField(max_length=50)
    modify_date = models.DateTimeField()
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_change"


class IndustryCommerceCheck(models.Model, Base):
    """工商-抽查检查
    """

    check_gov = models.CharField(max_length=50)
    check_type = models.CharField(max_length=20)
    check_date = models.DateTimeField()
    check_result = models.CharField(max_length=50)
    check_comment = models.CharField(max_length=50)
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_check"


class IndustryCommerceClear(models.Model, Base):
    """工商-清算
    """

    person_in_charge = models.CharField(max_length=30)
    persons = models.CharField(max_length=100)
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_clear"


class IndustryCommerceDetailGuarantee(models.Model, Base):
    """工商-动产抵押-详情-动产抵押
    """

    register_code = models.CharField(max_length=20)
    sharechange_register_date = models.DateTimeField()
    register_gov = models.CharField(max_length=50)
    register_id = models.CharField(max_length=20)
    ind_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_detail_guarantee"


class IndustryCommerceException(models.Model, Base):
    """工商-经营异常
    """

    list_on_reason = models.CharField(max_length=100)
    list_on_date = models.DateTimeField()
    list_out_reason = models.CharField(max_length=100)
    list_out_date = models.DateTimeField()
    list_gov = models.CharField(max_length=50)
    list_on_gov = models.CharField(max_length=50)
    list_out_gov = models.CharField(max_length=50)
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_exception"


class IndustryCommerceIllegal(models.Model, Base):
    """工商-严重违法
    """

    list_on_reason = models.CharField(max_length=100)
    list_on_date = models.DateTimeField()
    list_out_reason = models.CharField(max_length=100)
    list_out_date = models.DateTimeField(max_length=100)
    decision_gov = models.CharField(max_length=30)
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_illegal"


class IndustryCommerceMainperson(models.Model, Base):
    """工商-主要人员
    """

    name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_mainperson"


class IndustryCommerceMortgage(models.Model, Base):
    """工商-动产抵押登记
    """

    register_num = models.CharField(max_length=20)
    sharechange_register_date = models.DateTimeField()
    register_gov = models.CharField(max_length=50)
    guarantee_debt_amount = models.FloatField()
    status = models.CharField(max_length=20)
    publicity_time = models.DateTimeField()
    details = models.TextField()
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_mortgage"


class IndustryCommerceMortgageDetailChange(models.Model, Base):
    """工商-抵押-详情-变更
    """

    modify_date = models.DateTimeField()
    modify_content = models.TextField()
    register_id = models.CharField(max_length=20)
    ind_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_mortgage_detail_change"


class IndustryCommerceMortgageDetailGuarantee(models.Model, Base):
    """工商-抵押-详情-抵押权人
    """

    check_type = models.CharField(max_length=20)
    amount = models.FloatField()
    guarantee_scope = models.CharField(max_length=100)
    debtor_duration = models.CharField(max_length=20)
    comment = models.CharField(max_length=100)
    register_id = models.CharField(max_length=20)
    ind_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_cortgage_detail_guarantee"


class IndustryCommerceMortgageGuaranty(models.Model, Base):
    """工商-抵押-详情-抵押物
    """

    name = models.CharField(max_length=30)
    ownership = models.CharField(max_length=30)
    details = models.TextField()
    coments = models.CharField(max_length=100)
    register_id = models.CharField(max_length=20)
    ind_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_mortgage_guaranty"


class IndustryCommerceRevoke(models.Model, Base):
    """工商-撤销
    """

    revoke_item = models.CharField(max_length=30)
    content_before_revoke = models.CharField(max_length=50)
    content_after_revoke = models.CharField(max_length=50)
    revoke_date = models.DateTimeField()
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_revoke"


class IndustryCommerceShareholders(models.Model, Base):
    """工商-股东
    """

    shareholder_type = models.CharField(max_length=20)
    shareholder_name = models.CharField(max_length=30)
    certificate_type = models.CharField(max_length=20)
    certificate_number = models.CharField(max_length=20)
    subscription_amount = models.FloatField()
    paid_amount = models.FloatField()
    subscription_type = models.CharField(max_length=30)
    subscription_date = models.DateTimeField()
    subscription_money_amount = models.FloatField()
    paid_type = models.CharField(max_length=20)
    paid_money_amount = models.FloatField()
    paid_date = models.DateTimeField()
    enter_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_shareholders"


class IndustryCommerceSharepledge(models.Model, Base):
    """
    """

    register_num = models.CharField(max_length=20)
    pledgor = models.CharField(max_length=30)
    pledgor_certificate_code = models.CharField(max_length=20)
    share_pledge_num = models.FloatField()
    mortgagee = models.CharField(max_length=30)
    mortgagee_certificate_code = models.CharField(max_length=20)
    sharechange_register_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    change_detail = models.CharField(max_length=100)
    publicity_time = models.DateTimeField()
    modify_date = models.DateTimeField()
    modify_content = models.TextField()
    register_id = models.CharField(max_length=20)
    bas_id = models.IntegerField()

    class Meta:
        db_table = "industry_commerce_sharepledge"


class IndustryMortgageDetailMortgagee(models.Model, Base):
    """工商-抵押-详情-抵押权人
    """

    mortgagee_name = models.CharField(max_length=30)
    mortgagee_certificate_type = models.CharField(max_length=20)
    pledgor_certificate_code = models.CharField(max_length=20)
    register_id = models.CharField(max_length=20)
    ind_id = models.IntegerField()

    class Meta:
        db_table = "industry_mortgage_detail_mortgagee"
