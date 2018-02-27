# -*- coding: utf-8 -*-

from hl7apy import core
from hl7apy.consts import VALIDATION_LEVEL

hl7 = core.Message("ORM_O01", validation_level=VALIDATION_LEVEL.STRICT)

hl7.msh.msh_3 = "SendingApp"
hl7.msh.msh_4 = "SendingFac"
hl7.msh.msh_5 = "ReceivingApp"
hl7.msh.msh_6 = "ReceivingFac"
hl7.msh.msh_9 = "ORM^O01^ORM_O01"
hl7.msh.msh_10 = "168715"
hl7.msh.msh_11 = "P"

# PID
hl7.add_group("ORM_O01_PATIENT")
hl7.ORM_O01_PATIENT.pid.pid_2 = "1"
hl7.ORM_O01_PATIENT.pid.pid_3 = "A-10001"
hl7.ORM_O01_PATIENT.pid.pid_5 = "B-10001"
hl7.ORM_O01_PATIENT.pid.pid_6 = "DOE JOHN"

# PV1
hl7.ORM_O01_PATIENT.add_group("ORM_O01_PATIENT_VISIT")
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.add_segment("PV1")
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_1 = "2"
hl7.ORM_O01_PATIENT.ORM_O01_PATIENT_VISIT.PV1.pv1_2 = "3"

# ORC

hl7.ORM_O01_ORDER.orc.orc_1 = "1"
hl7.ORM_O01_ORDER.ORC.orc_10 = "20150414120000"

hl7.ORM_O01_ORDER.add_group("ORM_O01_ORDER_DETAIL")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.add_segment("ORM_O01_ORDER_CHOICE")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("OBR")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_1 = "1"
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_3 = "2"
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.OBR.obr_4 = "1100"
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("RQD")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("RQ1")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("RXO")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("ODS")
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.add_segment("ODT")

hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.ODS.ods_1 = ""
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.ODS.ods_3 = ""
hl7.ORM_O01_ORDER.ORM_O01_ORDER_DETAIL.ORM_O01_ORDER_CHOICE.ODT.odt_1 = ""

assert hl7.validate() is True

print hl7.value.replace('\r', '\n')
