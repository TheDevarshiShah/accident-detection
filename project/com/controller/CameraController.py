from flask import request, render_template, redirect, url_for
from project import app
from project.com.dao.AreaDAO import AreaDAO
from project.com.dao.CrossroadDAO import CrossroadDAO
from project.com.vo.CameraVO import CameraVO
from project.com.dao.CameraDAO import CameraDAO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


@app.route('/admin/loadCamera', methods=['GET'])
def adminLoadCamera():
    if adminLoginSession() == 'admin':
        areaDAO = AreaDAO()
        areaVOList = areaDAO.viewArea()
        crossroadDAO = CrossroadDAO()
        crossroadVOList = crossroadDAO.viewCrossroad()
        return render_template('admin/addCamera.html', areaVOList=areaVOList, crossroadVOList=crossroadVOList)


@app.route('/admin/insertCamera', methods=['POST'])
def adminInsertCamera():
    if adminLoginSession() == 'admin':
        cameraCode = request.form['cameraCode']
        camera_AreaId = request.form['camera_AreaId']
        camera_crossroadId = request.form['camera_CrossroadId']

        cameraVO = CameraVO()
        cameraDAO = CameraDAO()

        cameraVO.cameraCode = cameraCode
        cameraVO.camera_AreaId = camera_AreaId
        cameraVO.camera_CrossroadId = camera_crossroadId
        cameraDAO.insertCamera(cameraVO)

        return redirect(url_for('adminViewCamera'))


@app.route('/admin/viewCamera', methods=['GET'])
def adminViewCamera():
    if adminLoginSession() == 'admin':
        cameraDAO = CameraDAO()
        cameraVOList = cameraDAO.viewCamera()
        print("__________________", cameraVOList)
        return render_template('admin/viewCamera.html', cameraVOList=cameraVOList)
    else:
        return adminLogoutSession()


@app.route('/admin/deleteCamera', methods=['GET'])
def adminDeleteCamera():
    if adminLoginSession() == 'admin':
        cameraDAO = CameraDAO()
        cameraId = request.args.get('cameraId')
        cameraDAO.deleteCamera(cameraId)
        return redirect(url_for('adminViewCamera'))
    else:
        return adminLogoutSession()


@app.route('/admin/editCamera', methods=['get'])
def adminEditCamera():
    if adminLoginSession() == 'admin':

        cameraVO = CameraVO()
        cameraDAO = CameraDAO()

        crossroadDAO = CrossroadDAO()
        areaDAO = AreaDAO()

        cameraId = request.args.get('cameraId')
        cameraVO.cameraId = cameraId
        cameraVOList = cameraDAO.editCamera(cameraVO)
        crossroadVOList = crossroadDAO.viewCrossroad()
        print(crossroadVOList, '...')
        areaVOList = areaDAO.viewArea()
        return render_template('admin/editCamera.html', cameraVOList=cameraVOList, areaVOList=areaVOList,
                               crossroadVOList=crossroadVOList)
    else:
        return adminLogoutSession()


@app.route('/admin/updateCamera', methods=['POST'])
def adminUpdateCamera():
    if adminLoginSession() == 'admin':
        cameraCode = request.form['cameraCode']
        camera_AreaId = request.form['camera_AreaId']
        camera_CrossroadId = request.form['camera_CrossroadId']
        cameraId = request.form['cameraId']

        cameraVO = CameraVO()
        cameraDAO = CameraDAO()

        cameraVO.cameraId = cameraId
        cameraVO.cameraCode = cameraCode
        cameraVO.camera_AreaId = camera_AreaId
        cameraVO.camera_CrossroadId = camera_CrossroadId
        cameraDAO.updateCamera(cameraVO)
        return redirect(url_for('adminViewCamera'))
    else:
        return adminLogoutSession()


###user side Functions

