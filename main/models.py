from django.db import models


class Dogovory(models.Model):
    number = models.CharField(verbose_name='Договора', max_length=10)
    expir_date = models.DateField(verbose_name='Дата окончания договора', blank=True, null=True)
    usluga = models.ForeignKey("Uslugi", verbose_name='Услуга')
    saldo_in = models.DecimalField(max_digits=6, decimal_places=4, verbose_name='Входящее сальдо')
    saldo_out = models.DecimalField(max_digits=6, decimal_places=4, verbose_name='Исходящее сальдо')

    def __str__(self):
        return '%s' % self.number

    class Meta:
        verbose_name = 'Договора'


class Kvartiry(models.Model):
    kod_dom = models.ForeignKey("Dom", verbose_name='Дом')
    number = models.IntegerField(verbose_name='Номер квартиры')

    def __str__(self):
        return '%s - %s' % (self.number, self.kod_dom)

    class Meta:
        verbose_name = 'Квартиры'


class Dom(models.Model):
    nas_punkt = models.ForeignKey("Nas_punkt", verbose_name='Населенный пункт')
    street = models.ForeignKey("Street", verbose_name='Улица')
    number = models.IntegerField(verbose_name='Номер дома')
    index = models.CharField(max_length=1, verbose_name='Индекс дома', blank=True)
    korp = models.IntegerField(verbose_name='Корпус дома')
    prim = models.TextField(verbose_name='Примечание', blank=True)

    def __str__(self):
        return '%s, %s, %s' % (self.nas_punkt, self.street, self.number)

    class Meta:
        verbose_name = 'Дома'


class Lics(models.Model):
    lics = models.AutoField(verbose_name='Лицевой счет', primary_key=True)
    kod_dom = models.ForeignKey(Dom, verbose_name='Дом')
    kod_kvart = models.ForeignKey(Kvartiry, verbose_name='Квартира')
    tel = models.CharField(max_length=50, verbose_name="Телефон", blank=True)
    prim = models.TextField(verbose_name='Примечание', blank=True)
    email = models.CharField(max_length=20, verbose_name='Email', blank=True)
    dogovor = models.ForeignKey("Dogovory", verbose_name='Договор', default=0)

    def __str__(self):
        return '%s' % self.lics

    class Meta:
        verbose_name = 'Лицевые счета'


class Nas_punkt(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Населенные пункты'


class Street(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улицы'


class Person(models.Model):
    lics = models.ForeignKey(Lics, verbose_name='Лицевой счет')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    document = models.IntegerField(verbose_name='Вид документа',
                                   choices=(
                                       (1, 'Паспорт'),
                                       (2, 'Вид на жительство'),
                                       (3, "Справка")))
    document_number = models.CharField(max_length=20, verbose_name='Номер документа')
    dateOfBirdth = models.DateField(verbose_name='Дата рождения', auto_now=False, auto_now_add=False)
    dateOfDeath = models.DateField(verbose_name='Дата смерти', blank=True, auto_now=False, auto_now_add=False, null=True)
    gender = models.SmallIntegerField(verbose_name='Пол',
                                      choices=(
                                          (1, 'Мужской'),
                                          (2, 'Женский')
                                      ))
    prim = models.TextField(verbose_name='Примечание', blank=True)

    def __str__(self):
        return '%s, %s %s' % (self.lics, self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Физические лица'


class Lgoty(models.Model):
    person = models.ForeignKey(Person, verbose_name='Физ лицо')
    tip_lgoty = models.ForeignKey('Tip_lgoty', verbose_name='Тип льготы')
    number = models.CharField(max_length=20, verbose_name='Серия и номер льготы')
    skidka = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Скидка', default=0)

    def __str__(self):
        return '%s' % self.person

    class Meta:
        verbose_name = 'Льготы'


class Tip_lgoty(models.Model):
    name = models.TextField(verbose_name='Наименование льготы')
    date_in = models.DateField(verbose_name='Дата начала действия льготы', blank=True, null=True)
    date_out = models.DateField(verbose_name='Дата окончания действия льготы', blank=True, null=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Типы льгот'


class Uslugi(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    pricing = models.DecimalField(max_digits=6, decimal_places=4, verbose_name='Расценка')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Услуги'


class MarkiPriborov(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    manufacturer = models.CharField(max_length=50, verbose_name='Производитель', blank=True)
    expir_date = models.DateField(verbose_name='Срок действия')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Марки приборов учета'


class Pribory(models.Model):
    kod_uslugi = models.ForeignKey(Uslugi, verbose_name='Услуга')
    kod_pribor = models.ForeignKey(MarkiPriborov, verbose_name='Марка прибора')
    sn = models.CharField(max_length=100, verbose_name='Серийный номер')
    date_poverky = models.DateField(verbose_name="Дата последней поверки")
    value = models.IntegerField(verbose_name="Показания счетчика", default=0)
    oplata = models.BooleanField(verbose_name='Оплачено?', default=False)

    def __str__(self):
        return '%s %s - %s' % (self.id, self.kod_pribor, self.kod_uslugi)

    class Meta:
        verbose_name = 'Приборы учета'


class Pribor_Lics(models.Model):
    lics = models.ForeignKey(Lics, verbose_name='Лицевой счет')
    pribor = models.OneToOneField(Pribory, verbose_name='Приборы учета', default=0)

    def __str__(self):
        return '%s' % self.lics

    class Meta:
        verbose_name = 'Связь приборов учета с лицевыми счетами'
