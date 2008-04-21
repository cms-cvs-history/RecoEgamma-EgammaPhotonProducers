import FWCore.ParameterSet.Config as cms

# KFUpdatoerESProducer
from TrackingTools.KalmanUpdators.KFUpdatorESProducer_cfi import *
from RecoEgamma.EgammaPhotonProducers.propAlongMomentumWithMaterialForElectrons_cfi import *
from RecoEgamma.EgammaPhotonProducers.KFFittingSmootherForInOut_cfi import *
ckfInOutTracksFromConversions = cms.EDFilter("TrackProducerWithSCAssociation",
    src = cms.InputTag("conversionTrackCandidates","inOutTracksFromConversions"),
    recoTrackSCAssociationCollection = cms.string('inOutTrackSCAssociationCollection'),
    producer = cms.string('conversionTrackCandidates'),
    Fitter = cms.string('KFFittingSmootherForInOut'),
    useHitsSplitting = cms.bool(False),
    trackCandidateSCAssociationCollection = cms.string('inOutTrackCandidateSCAssociationCollection'),
    TrajectoryInEvent = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    #string AlgorithmName = "ecalSeededConv"
    AlgorithmName = cms.string('undefAlgorithm'),
    ComponentName = cms.string('ckfInOutTracksFromConversions'),
    #string Propagator = "PropagatorWithMaterial"
    Propagator = cms.string('alongMomElePropagator'),
    beamSpot = cms.InputTag("offlineBeamSpot")
)


