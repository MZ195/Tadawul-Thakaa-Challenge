from django.db import models
import pymongo
import psycopg2

# Create your models here.

client = pymongo.MongoClient(
    "mongodb+srv://Mezo:Almazni2013@tadawul-test.wkg8i.mongodb.net/Tadawul_v3?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

#Create database connection postgres://ytvwlxfp:DQWgHzUZE_ormYbJ1UHzBJ_yatJCcss6@chunee.db.elephantsql.com/ytvwlxfp
# postgresSQL = psycopg2.connect(
#     database="ytvwlxfp",
#                 user="ytvwlxfp",
#                 password="DQWgHzUZE_ormYbJ1UHzBJ_yatJCcss6",
#                 host="chunee.db.elephantsql.com",
#                 port="5432"
#                 )

#  below is the auto-generated Django model of our postgresql database 

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
class AssetTurnoverRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_turnover_ratio'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookValue(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_value'


class CashChange(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_change'


class CashConversionCycle(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_conversion_cycle'


class CashRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_ratio'


class CompaniesGeneral(models.Model):
    ticker = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    authorized_capital = models.FloatField(blank=True, null=True)
    issued_shares = models.FloatField(blank=True, null=True)
    paid_capital = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies_general'


class CurrentAssets(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_assets'


class CurrentRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_ratio'


class DaysInventoryOutstanding(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'days_inventory_outstanding'


class DaysPayableOutstanding(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'days_payable_outstanding'


class DaysSalesOutstanding(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'days_sales_outstanding'


class DebtRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debt_ratio'


class DebtToEquity(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debt_to_equity'


class DividendYield(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dividend_yield'
class DividendIndustryAverage(models.Model):
    id = models.AutoField(primary_key=True)
    sector = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    Average = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dividend_Industry_Average'

class DividendsPerShare(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dividends_per_share'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ebit(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebit'


class Ebitda(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebitda'


class Eps(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eps'


class EquityToCapital(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equity_to_capital'


class EquityTurnoverRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equity_turnover_ratio'


class InventoryTurnoverRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_turnover_ratio'


class Marketcap(models.Model):
    ticker = models.IntegerField(primary_key=True)
    marketcap = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketcap'


class NetFixedAssetTurnoverRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'net_fixed_asset_turnover_ratio'


class NetMargin(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'net_margin'


class NonCurrentAssets(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_current_assets'


class OperatingCycle(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operating_cycle'


class OperatingEps(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operating_eps'


class OperatingProfitMargin(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operating_profit_margin'


class OperatingProfitMultiple(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operating_profit_multiple'


class PayableTurnoverRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payable_turnover_ratio'


class PayoutRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payout_ratio'


class Pb(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pb'


class Pe(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pe'


class Ps(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps'


class QuickRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quick_ratio'


class ReceivablesTurnoverRatio(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receivables_turnover_ratio'


class Roa(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roa'


class Roe(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roe'


class Rota(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rota'


class TotalLiabilities(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.IntegerField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_liabilities'


