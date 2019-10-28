from enum import Enum
from typing import Dict

class fileType(Enum):
    blank = 0
    SAP9502 = 1
    SAP9532 = 2
    SAPHierarchy = 3
    TOPRS = 4
    T110 = 5
    SAP9000 = 6
    YOYAdj = 7
    FieldRollup = 8
    TOPRSPlan = 9
    SAPYOYAdj = 10
    RestructureActuals = 11
    RestructureTarget = 12
    T313 = 13
    T008 = 14
    WC2CC = 15
    LastPlanA = 16
    Weekly1508 = 17
    SAP9502_WKLY = 18
    SAP9000_DLM = 19
    HHBonus = 20
    TOPRSRollup = 21

class fileFormat(Enum):
    csv = 1
    xl = 2
    T110 = 3
    TOPRS = 4


fileType_dictionary: Dict[str, fileType] = {"SAP9502": fileType.SAP9502,
                                                "SAP9532": fileType.SAP9532,
                                                "TOPRS": fileType.TOPRS,
                                                "SAP9000": fileType.SAP9000,
                                                "TOPRSPlan": fileType.TOPRSPlan,
                                                "RestructureActuals": fileType.RestructureActuals,
                                                "RestructureTarget": fileType.RestructureTarget,
                                                "T313": fileType.T313,
                                                "T008": fileType.T008,
                                                "T110": fileType.T110,
                                                "FieldRollup": fileType.FieldRollup,
                                                "WorkCenterToCostCentre": fileType.WC2CC,
                                                "LastPlanA": fileType.LastPlanA,
                                                "Weekly1508": fileType.Weekly1508,
                                                "SAP9502_WKLY": fileType.SAP9502_WKLY,
                                                "SAP9000_DLM": fileType.SAP9000_DLM,
                                                'HHBonus': fileType.HHBonus,
                                                'TOPRSRollup': fileType.TOPRSRollup}

fileFormat_dictionary: Dict[fileType, fileFormat] = { fileType.SAP9502 : fileFormat.csv,
                                                fileType.SAP9532 : fileFormat.csv,
                                                fileType.TOPRS : fileFormat.TOPRS,
                                                fileType.SAP9000 : fileFormat.csv,
                                                fileType.TOPRSPlan : fileFormat.xl,
                                                fileType.RestructureActuals : fileFormat.xl,
                                                fileType.RestructureTarget : fileFormat.xl,
                                                fileType.T313 : fileFormat.xl,
                                                fileType.T008 : fileFormat.xl,
                                                fileType.T110 : fileFormat.xl,
                                                fileType.FieldRollup : fileFormat.xl,
                                                fileType.WC2CC : fileFormat.xl,
                                                fileType.LastPlanA : fileFormat.xl,
                                                fileType.Weekly1508 : fileFormat.xl,
                                                fileType.SAP9502_WKLY : fileFormat.csv,
                                                fileType.SAP9000_DLM : fileFormat.csv,
                                                fileType.HHBonus : fileFormat.xl,
                                                fileType.TOPRSRollup : fileFormat.xl}

fileTypeList = {"SAP9502", "SAP9532", "TOPRS", "SAP9000", "TOPRSPlan", "RestructureActuals", "RestructureTarget",
                    "T313", "T008", "T110", "FieldRollup", "WorkCenterToCostCentre", "LastPlanA", "Weekly1508",
                "SAP9502_WKLY","SAP9000_DLM", 'HHBonus', 'TOPRSRollup'}

TOPRSskipSheets = ["TemplateLanguage", "NatOrvLanguageTemplate", "OvrLanguageTemplate", "RSMCOvrLanguageTemplate",
              "WoprsLanguageTemplate", "Graphs", "Overview | Sommaire", "Exp", "RSMC Overview | Sommaire FFRS",
              "WOPRS", "WOPRS Data"]