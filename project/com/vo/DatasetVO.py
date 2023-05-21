from project import db


class DatasetVO(db.Model):
    __tablename__ = 'datasetmaster'
    datasetId = db.Column('datasetId', db.Integer, primary_key=True, autoincrement=True)
    datasetFileName = db.Column('datasetFileName', db.String(100))
    datasetFilePath = db.Column('datasetFilePath', db.String(100))
    datasetUploadTime = db.Column('datasetUploadTime', db.String(100))
    datasetUploadDate = db.Column('datasetUploadDate', db.String(100))

    def as_dict(self):
        return {
            'datasetId': self.areaId,
            'datasetFileName': self.datasetFileName,
            'datasetFilePath':self.datasetFilePath,
            'datasetUploadTime': self.datasetUploadTime,
            'datasetUploadDate': self.datasetUploadDate

        }


db.create_all()
