from FileEnums import fileType
from typing import Dict

startRow_dictionary: Dict[fileType, int] = { fileType.SAP9502 : 5,
                                            fileType.SAP9532 : 5,
                                            fileType.SAPHierarchy : 2,
                                            fileType.TOPRS : 8 ,
                                            fileType.SAP9000 : 5,
                                            fileType.YOYAdj : 2,
                                            fileType.FieldRollup : 2,
                                            fileType.TOPRSPlan : 2,
                                            fileType.SAPYOYAdj : 5,
                                            fileType.RestructureActuals : 2,
                                            fileType.RestructureTarget : 2,
                                            fileType.T313 : 2,
                                            fileType.T008 : 2,
                                            fileType.WC2CC : 2,
                                            fileType.LastPlanA : 2,
                                            fileType.Weekly1508 : 2,
                                            fileType.SAP9502_WKLY: 5,
                                            fileType.SAP9532_WKLY: 5,
                                            fileType.SAP9000_DLM: 5,
                                            fileType.HHBonus: 5,
                                            fileType.TOPRSRollup: 2,
                                            fileType.DLM_BWHours_Period: 5,
                                            fileType.DLM_BWHours_Weekly: 5,
                                            fileType.DLM_BWDollars: 5,
                                            fileType.T110 : 3,
                                            fileType.DLM_Hierarchy_Eng: 3}

XLsheetDictionary: Dict[fileType, str] = {  fileType.SAPHierarchy : 'Rollup for R3HIER E',
                                            fileType.YOYAdj : 'Summary_CDMP',
                                            fileType.FieldRollup : 'Field Rollup',
                                            fileType.TOPRSPlan : 'Target Hours',
                                            fileType.RestructureActuals : 'Depot Report_Consolidated',
                                            fileType.RestructureTarget : 'Depot Report_Consolidated',
                                            fileType.T313 : 'data',
                                            fileType.T008 : 'Sheet1',
                                            fileType.WC2CC : 'Valid',
                                            fileType.LastPlanA : 'Depots',
                                            fileType.Weekly1508 : 'Weekly Data',
                                            fileType.TOPRSRollup : 'Short TOPRS',
                                            fileType.DLM_Hierarchy_Eng : 'Rollup for R3HIER E'}

T110sheetDictionary: Dict[str, str] = {'Hours' : 'Data_Hrs',
                                       'Dollars' : 'Data_Dollars'}