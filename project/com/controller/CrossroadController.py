from flask import request, render_template, redirect, url_for
from project import app
from project.com.dao.AreaDAO import AreaDAO
from project.com.dao.CrossroadDAO import CrossroadDAO
from project.com.vo.CrossroadVO import CrossroadVO
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


@app.route('/admin/loadCrossroad', methods=['GET'])
def adminLoadCrossroad():
    if adminLoginSession() == 'admin':
        areaDAO = AreaDAO()
        areaVOList = areaDAO.viewArea()
        return render_template('admin/addCrossroad.html',areaVOList=areaVOList)
    else:
        return adminLogoutSession()


@app.route('/admin/insertCrossroad', methods=['POST'])
def adminInsertCrossroad():
    if adminLoginSession() == 'admin':
        crossroadName = request.form['crossroadName']
        crossroad_AreaId=request.form['crossroad_AreaId']

        crossroadVO = CrossroadVO()
        crossroadDAO = CrossroadDAO()

        crossroadVO.crossroadName = crossroadName
        crossroadVO.crossroad_AreaId=crossroad_AreaId

        crossroadDAO.insertCrossroad(crossroadVO)

        return redirect(url_for('adminViewCrossroad'))
    else:
        return adminLogoutSession()


@app.route('/admin/viewCrossroad')
def adminViewCrossroad():
    if adminLoginSession() == 'admin':
        crossroadDAO = CrossroadDAO()
        crossroadVOList = crossroadDAO.viewCrossroad()
        print("__________________", crossroadVOList)
        return render_template('admin/viewCrossroad.html', crossroadVOList=crossroadVOList)
    else:
        return adminLogoutSession()



@app.route('/admin/deleteCrossroad', methods=['GET'])
def adminDeleteCrossroad():
    if adminLoginSession() == 'admin':

        crossroadDAO = CrossroadDAO()

        crossroadId=request.args.get('crossroadId')

        crossroadDAO.deleteCrossroad(crossroadId)

        return redirect(url_for('adminViewCrossroad'))
    else:
        return adminLogoutSession()


@app.route('/admin/editCrossroad', methods=['get'])
def adminEditCrossroad():
    if adminLoginSession() == 'admin':

        crossroadVO = CrossroadVO()
        crossroadDAO = CrossroadDAO()
        areaDAO = AreaDAO()

        crossroadId = request.args.get('crossroadId')
        print('crossroadId:::',crossroadId)

        crossroadVOList=crossroadDAO.viewCrossroad()
        print('crossroadVOList::',crossroadVOList)

        areaVOList = areaDAO.viewArea()
        print('areaVOList::',areaVOList)

        return render_template('admin/editCrossroad.html',areaVOList=areaVOList,crossroadVOList=crossroadVOList)
    else:
        return adminLogoutSession()


@app.route('/admin/updateCrossroad', methods=['POST'])
def adminUpdateCrossroad():
    if adminLoginSession() == 'admin':
        crossroadName = request.form['crossroadName']
        crossroad_AreaId = request.form['crossroad_AreaId']
        crossroadId=request.form['crossroadId']

        crossroadVO = CrossroadVO()
        crossroadDAO = CrossroadDAO()

        crossroadVO.crossroadId=crossroadId
        crossroadVO.crossroadName = crossroadName
        crossroadVO.crossroad_AreaId = crossroad_AreaId

        crossroadDAO.updateCrossroad(crossroadVO)

        return redirect(url_for('adminViewCrossroad'))
    else:
        return adminLogoutSession()
