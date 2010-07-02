import FWCore.ParameterSet.Config as cms

postProcessorEventGenerator = cms.EDAnalyzer(
    "DQMGenericClient",
    subDirs = cms.untracked.vstring("Generator/MBUEandQCD*"),
    efficiency = cms.vstring(""),
    resolution = cms.vstring(""),
    normalization = cms.untracked.vstring("nNoFwdTrig nEvt",
                                          "nSaFwdTrig nEvt",
                                          "nbquark nEvt",
                                          "ncandbquark nEvt",
                                          "ncnobquark nEvt",
                                          "dNchdpt1 nEvt1",
                                          "dnChdeta1 nEvt1",
                                          "leadTrackpt nEvt2",
                                          "leadTracketa nEvt2",
                                          "dNchdpt2 nEvt2",
                                          "dNchdeta2 nEvt2",
                                          "nCha nEvt2",
                                          "dNchdSpt nEvt2",
                                          "nChj nEvt2",
                                          "dNchjdeta nEvt2",
                                          "dNchjdpt nEvt2",
                                          "leadChjpt nEvt2",
                                          "leadChjeta nEvt2",
                                          "nPPbar nEvt2",
                                          "nKpm nEvt2",
                                          "nK0s nEvt2",
                                          "nL0 nEvt2",
                                          "nXim nEvt2",
                                          "nOmega nEvt2",
                                          "pPPbar nEvt2",
                                          "pKpm nEvt2",
                                          "pK0s nEvt2",
                                          "pL0 nEvt2",
                                          "pXim nEvt2",
                                          "pOmega nEvt2",
                                          "nNNbar nEvt2",
                                          "nGamma nEvt2",
                                          "pNNbar nEvt2",
                                          "pGamma nEvt2",
                                          "elePt nEvt2",
                                          "muoPt nEvt2",
                                          "nDijet nHFflow",
                                          "nj nHFflow",
                                          "dNjdeta nHFflow",
                                          "dNjdpt nHFflow",
                                          "pt1pt2balance nHFflow",
                                          "pt1pt2Dphi nHFflow",
                                          "pt1pt2InvM nHFflow",
                                          "pt3Frac nHFflow",
                                          "sumJEt nHFflow",
                                          "missEtosumJEt nHFflow",
                                          "sumPt nHFflow",
                                          "sumChPt nHFflow",
                                          "EmpzHFm nHFSD",
                                          "ntHFm nHFSD",
                                          "eneHFmSel nHFSD",
                                          "_JM25njets nHFflow",
                                          "_JM25ht nHFflow",
                                          "_JM25pt1 nHFflow",
                                          "_JM25pt2 nHFflow",
                                          "_JM25pt3 nHFflow",
                                          "_JM25pt4 nHFflow",
                                          "_JM80njets nHFflow",
                                          "_JM80ht nHFflow",
                                          "_JM80pt1 nHFflow",
                                          "_JM80pt2 nHFflow",
                                          "_JM80pt3 nHFflow",
                                          "_JM80pt4 nHFflow",
                                          "djr10 nEvt",
                                          "djr21 nEvt",
                                          "djr32 nEvt",
                                          "djr43 nEvt",
                                          "_sumEt nEvt",
                                          "_sumEt1 nEvt",
                                          "_sumEt2 nEvt",
                                          "_sumEt3 nEvt",
                                          "_sumEt4 nEvt", 
                                          "_sumEt5 nEvt",
                                          "nEvt1 nEvt",
                                          "nEvt2 nEvt",
                                          "nHFflow nEvt",
                                          "nHFSD nEvt"),
    cumulativeDists = cms.untracked.vstring(""),
    outputFileName = cms.untracked.string("")
)        

EventGeneratorPostProcessor = cms.Sequence(postProcessorEventGenerator)
