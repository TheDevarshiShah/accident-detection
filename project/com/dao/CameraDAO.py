from project import db
from project.com.vo.AreaVO import AreaVO
from project.com.vo.CrossroadVO import CrossroadVO
from project.com.vo.CameraVO import CameraVO

class CameraDAO:
    def insertCamera(self,cameraVO):

        db.session.add(cameraVO)

        db.session.commit()

    def viewCamera(self):
        cameraList = db.session.query(CameraVO,CrossroadVO, AreaVO).join(AreaVO,CameraVO.camera_AreaId == AreaVO.areaId).join(CrossroadVO,CameraVO.camera_CrossroadId==CrossroadVO.crossroadId).all()

        return cameraList

    def deleteCamera(self, cameraId):

        cameraList = CameraVO.query.get(cameraId)

        db.session.delete(cameraList)

        db.session.commit()

    def editCamera(self, cameraVO):
        cameraList = CameraVO.query.filter_by(cameraId=cameraVO.cameraId)

        return cameraList

    def updateCamera(self, cameraVO):

        db.session.merge(cameraVO)

        db.session.commit()

    def ajaxCameraProduct(self, cameraVO):

        ajaxProductCameraList = CameraVO.query.filter_by(camera_AreaId=cameraVO.camera_AreaId,camera_CrossroadId=cameraVO.camera_CrossroadId).all()

        return ajaxProductCameraList
