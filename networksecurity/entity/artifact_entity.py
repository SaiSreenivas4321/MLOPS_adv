from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    pass


@dataclass
class DataValidationArtifact:
    pass


@dataclass
class DataTransformationArtifact:
    pass


@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModelEvalutionArtifact:
    pass


@dataclass
class ModelPusherArtifact:
    pass
