from django.db import models

class ControllerInput(models.Model):
    a = models.IntegerField(default = 0) #nned to include these default values so the server is happy
    b = models.IntegerField(default = 0)
    x = models.IntegerField(default = 0)
    y = models.IntegerField(default = 0)
    st = models.IntegerField(default = 0)
    se = models.IntegerField(default = 0)
    rt = models.IntegerField(default = 0)
    lt = models.IntegerField(default = 0)
    rb = models.IntegerField(default = 0)
    lb = models.IntegerField(default = 0)
    rsx = models.IntegerField(default = 0)
    rsy = models.IntegerField(default = 0)
    lsx = models.IntegerField(default = 0)
    lsy = models.IntegerField(default = 0)
    u = models.IntegerField(default = 0)
    d = models.IntegerField(default = 0)
    l = models.IntegerField(default = 0)
    r = models.IntegerField(default = 0)
    hl = models.IntegerField(default = 0)
    lim = models.IntegerField(default = 50)
    

    def __str__(self):
        val = "a: {} | b: {} | x: {} | y: {} | st: {} | se: {}\n".format(self.a, self.b, self.x, self.y, self.st, self.se)
        val += "rt: {} | lt: {} | rb: {} | lb: {}\n".format(self.rt, self.lt, self.rb, self.lb)
        val += "rsx: {} | rsy: {} | lsx: {} | lsy: {}".format(self.rsx, self.rsy, self.lsx, self.lsy)
        val += "u: {} | d: {} | l: {} | r: {}".format(self.u, self.d, self.l, self.r)
        val += "hl: {} | lim: {}".format(self.hl, self.lim)
        return val

    def createDictionary(self):
        value = {
        'a':self.a, 'b': self.b, 'x': self.x, 'y': self.y, 'st': self.st, 'se': self.se,
        'rt': self.rt, 'lt': self.lt, 'rb': self.rb, 'lb': self.lb,
        'rsx': self.rsx, 'rsy': self.rsy, 'lsx': self.lsx, 'lsy': self.lsy,
        'u': self.u, 'd': self.d, 'l': self.l, 'r': self.r,
        'hl': self.hl, 'lim': self.lim
        }
        return value