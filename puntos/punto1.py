# -*- coding: utf-8 -*-
"""
Una Institución educativa ha recibido una donación especial que será
repartida entre las carreras de Telecomunicaciones, Sistemas,
Administración y Contabilidad de la siguiente forma:
a. Telecomunicaciones 10% del valor dado a sistemas
b. Sistemas: 25% del valor dado a Administración
c. Administración: 35% del valor de la donación
d. Contabilidad: lo que resta de la donación

"""
donacion_institucion = int(input("Escriba el valor de la donación : "));
admin = donacion_institucion*0.35;
sistemas = admin*0.25;
teleco = sistemas*0.1;
restante = donacion_institucion - (admin+sistemas+teleco);
conta = donacion_institucion - restante
print("Donacion  de la institucion: {} \n".format(donacion_institucion));
print("Donacion a administracion : {} \n".format(admin));
print("Donacion a sistemas : {}\n".format(sistemas));
print("Donacion  a telecomucion: {}\n".format(teleco));
print("Donacion a contabilidad : {}".format(conta));





