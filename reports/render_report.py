from rest_framework.response import Response
from rest_framework import status

from common.time_conversor import TimeConversor
from common.privilege import Privilege
from common.report import Report

import reports.serializers as report_serializers
from geofences.models import Geofence

time_conversor = TimeConversor()
privilege = Privilege()
report = Report()

class RenderReport:

    def render_detailed_report(self,request):
        data = request.data
        serializer = report_serializers.ReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 604800:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            try:
                unit = units.get(id=int(data['unitid']))
            except Exception as e:
                error = {
                    'detail':str(e)
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
        serializer = report_serializers.ReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                harsh_driving_report = []
                summarization = []
                for unit in units:
                    unit_harsh_driving_report = report.generate_driving_style_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                    )
                    for uhdr in unit_harsh_driving_report['harsh_driving_report']:
                        harsh_driving_report.append(uhdr)
                    for uhdr in unit_harsh_driving_report['summarization']:
                        print(uhdr)
                        summarization.append(uhdr)
                response = {
                    'harsh_driving_report':harsh_driving_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except:
                    error = {
                        'detail':str(e)
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
        serializer = report_serializers.SpeedReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
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
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
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
        serializer = report_serializers.TripReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                trip_report = []
                summarization = []
                for unit in units:
                    unit_trip_report = report.generate_trip_report1(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        data['geofence_option'],
                    )
                    for utr in unit_trip_report['trip_report']:
                        trip_report.append(utr)
                    for utr in unit_trip_report['summarization']:
                        summarization.append(utr)
                response = {
                    'trip_report':trip_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
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
        data = request.data
        serializer = report_serializers.TripReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                trip_report = []
                summarization = []
                for unit in units:
                    unit_trip_report = report.generate_trip_report2(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        data['geofence_option'],
                    )
                    for utr in unit_trip_report['trip_report']:
                        trip_report.append(utr)
                    for utr in unit_trip_report['summarization']:
                        summarization.append(utr)
                response = {
                    'trip_report':trip_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_trip_report2(
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

    def render_mileage_report(self,request):
        data = request.data
        serializer = report_serializers.ReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                total_mileage = []
                mileage_by_date = []
                for unit in units:
                    unit_mileage_report = report.generate_mileage_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                    )
                    for umr in unit_mileage_report['total_mileage']:
                        total_mileage.append(umr)
                    for umr in unit_mileage_report['mileage_by_date']:
                        mileage_by_date.append(umr)
                response = {
                    'total_mileage':total_mileage,
                    'mileage_by_date':mileage_by_date,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_mileage_report(
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

    def render_geofence_report(self,request):
        data = request.data
        serializer = report_serializers.GeofenceReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            geofences = []
            for i in range(len(data['geofences'])):
                try:
                    geofence = Geofence.objects.get(
                        id = data['geofences'][i],
                        account = request.user.profile.account,
                    )
                    geofences.append(geofence)
                except Exception as e:
                    pass
            if len(geofences) == 0:
                error = {
                    'detail': 'There are no geofences'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                geofence_report = []
                for unit in units:
                    unit_geofence_report =report.generate_geofence_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        geofences,
                    )
                    for ugr in unit_geofence_report:
                        geofence_report.append(ugr)
                return Response(geofence_report,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_geofence_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        geofences,
                    ),
                    status=status.HTTP_200_OK
                )
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    def render_stop_report(self,request):
        data = request.data
        serializer = report_serializers.StopReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            discard_time = int(data['discard_time'])*60
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                stop_report = []
                summarization = []
                for unit in units:
                    unit_stop_report = report.generate_stop_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        data['geofence_option'],
                        discard_time,
                    )
                    for usr in unit_stop_report['stop_report']:
                        stop_report.append(usr)
                    for usr in unit_stop_report['summarization']:
                        summarization.append(usr)
                response = {
                    'stop_report':stop_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_stop_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                        data['geofence_option'],
                        discard_time,
                    ),
                    status=status.HTTP_200_OK
                )
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    def render_temperature_report(self,request):
        data = request.data
        serializer = report_serializers.ReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                temperature_report = []
                summarization = []
                for unit in units:
                    unit_temperature_report = report.generate_temperature_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                    )
                    for utr in unit_temperature_report['temperature_report']:
                        temperature_report.append(utr)
                    for utr in unit_temperature_report['summarization']:
                        summarization.append(utr)
                response = {
                    'temperature_report':temperature_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_temperature_report(
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

    def render_hours_report(self,request):
        data = request.data
        serializer = report_serializers.ReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                hours_report = []
                summarization = []
                for unit in units:
                    unit_hours_report = report.generate_hours_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                    )
                    for uhr in unit_hours_report['hours_report']:
                        unit_hours_report.append(uhr)
                    for uhr in unit_hours_report['summarization']:
                        summarization.append(uhr)
                response = {
                    'hours_report':hours_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_hours_report(
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

    def render_telemetry_report(self,request):
        data = request.data
        serializer = report_serializers.ReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = privilege.get_units(request)
            if int(data['unitid']) == 0:
                telemetry_report = []
                summarization = []
                for unit in units:
                    unit_telemetry_report = report.generate_telemetry_report(
                        unit,
                        initial_timestamp,
                        final_timestamp,
                    )
                    for utr in unit_telemetry_report['telemetry_report']:
                        unit_telemetry_report.append(utr)
                    for utr in unit_telemetry_report['summarization']:
                        summarization.append(utr)
                response = {
                    'telemetry_report':telemetry_report,
                    'summarization':summarization,
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                try:
                    unit = units.get(id=int(data['unitid']))
                except Exception as e:
                    error = {
                        'detail':str(e)
                    }
                    return Response(error,status=status.HTTP_400_BAD_REQUEST)
                return Response(
                    report.generate_telemetry_report(
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

    def render_group_driving_style_report(self,request):
        data = request.data
        serializer = report_serializers.GroupReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            try:
                groups = privilege.get_groups(request)
                group = groups.get(id=int(data['groupid']))
            except Exception as e:
                error = {
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = group.units.all()
            harsh_driving_report = []
            summarization = []
            for unit in units:
                unit_harsh_driving_report = report.generate_driving_style_report(
                    unit,
                    initial_timestamp,
                    final_timestamp,
                )
                for item in unit_harsh_driving_report['harsh_driving_report']:
                    harsh_driving_report.append(item)
                for item in unit_harsh_driving_report['summarization']:
                    summarization.append(item)
            response = {
                'harsh_driving_report':harsh_driving_report,
                'summarization':summarization,
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)

    def render_group_speed_report(self,request):
        data = request.data
        serializer = report_serializers.GroupSpeedReportSerializer(data=data)
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
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            if final_timestamp - initial_timestamp > 2678400:
                error = {
                    'detail': 'Report time range exceeded.'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            try:
                groups = privilege.get_groups(request)
                group = groups.get(id=int(data['groupid']))
            except Exception as e:
                error = {
                    'detail':str(e)
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
            units = group.units.all()
            speed_report = []
            summarization = []
            for unit in units:
                unit_speed_report = report.generate_speed_report(
                    unit,
                    initial_timestamp,
                    final_timestamp,
                    int(data['speed_limit']),
                )
                for item in unit_speed_report['speed_report']:
                    speed_report.append(item)
                for item in unit_speed_report['summarization']:
                    summarization.append(item)
            response = {
                'speed_report':speed_report,
                'summarization':summarization,
            }
            return Response(response,status=status.HTTP_200_OK)
        else:
            error = {
                'errors':serializer.errors
            }
            return Response(error,status=status.HTTP_400_BAD_REQUEST)