from rest_framework.response import Response
from rest_framework import status

from common.time_conversor import TimeConversor
from common.privilege import Privilege
from common.report import Report

from .serializers import ReportSerializer,SpeedReportSerializer,TripReportSerializer

time_conversor = TimeConversor()
privilege = Privilege()
report = Report()

class RenderReport:

    def render_detailed_report(self,request):
        data = request.data
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            try:
                initial_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['initial_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
                final_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['final_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 604800:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request.user.profile)
            try:
                unit = units.get(name=data['unit_name'])
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            return Response(
                report.generate_detailed_report(
                    unit,
                    initial_timestamp,
                    final_timestamp,
                ),
                status=status.HTTP_200_OK
            )
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    def render_driving_style_report(self,request):
        data = request.data
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            try:
                initial_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['initial_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
                final_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['final_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 604800:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request.user.profile)
            try:
                unit = units.get(name=data['unit_name'])
            except:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            return Response(
                report.generate_driving_style_report(
                    unit,
                    initial_timestamp,
                    final_timestamp,
                ),
                status=status.HTTP_200_OK
            )
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    def render_speed_report(self,request):
        data = request.data
        serializer = SpeedReportSerializer(data=data)
        if serializer.is_valid():
            try:
                initial_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['initial_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
                final_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['final_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 604800:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request.user.profile)
            if data['unit_name'].upper() == 'ALL':
                speed_report = []
                summarization = []
                for unit in units:
                    unit_speed_report = report.generate_speed_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        data['speed_limit']
                    )
                    for usr in unit_speed_report['speed_report']:
                        speed_report.append(usr)
                    for usr in unit_speed_report['summarization']:
                        summarization.append(usr)
                response = {
                    'speed_report':speed_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(name=data['unit_name'])
                except Exception as e:
                    error = {
                        'error':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_speed_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        data['speed_limit']
                    ),
                    status=status.HTTP_200_OK
                )
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    def render_trip_report1(self,request):
        data = request.data
        serializer = TripReportSerializer(data=data)
        if serializer.is_valid():
            try:
                initial_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['initial_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
                final_timestamp = time_conversor.convert_local_datetimestr_to_utc_timestamp(
                    data['final_datetime'],
                    '%Y-%m-%d %H:%M:%S'
                )
            except Exception as e:
                error = {
                    'error':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 604800:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request.user.profile)
            if data['unit_name'].upper() == 'ALL':
                speed_report = []
                summarization = []
                for unit in units:
                    pass
                response = {
                    'speed_report':speed_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(name=data['unit_name'])
                except Exception as e:
                    error = {
                        'error':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_trip_report1(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        data['geofence_option'],
                    ),
                    status=status.HTTP_200_OK
                )
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    def render_trip_report2(self,request):
        pass