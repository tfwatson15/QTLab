from ctypes import *
import numpy as np
import time

DRV_ERROR_CODES = 20001
DRV_SUCCESS = 20002
DRV_VXDNOTINSTALLED = 20003
DRV_ERROR_SCAN = 20004
DRV_ERROR_CHECK_SUM = 20005
DRV_ERROR_FILELOAD = 20006
DRV_UNKNOWN_FUNCTION = 20007
DRV_ERROR_VXD_INIT = 20008
DRV_ERROR_ADDRESS = 20009
DRV_ERROR_PAGELOCK = 20010
DRV_ERROR_PAGEUNLOCK = 20011
DRV_ERROR_BOARDTEST = 20012
DRV_ERROR_ACK = 20013
DRV_ERROR_UP_FIFO = 20014
DRV_ERROR_PATTERN = 20015

DRV_ACQUISITION_ERRORS = 20017
DRV_ACQ_BUFFER = 20018
DRV_ACQ_DOWNFIFO_FULL = 20019
DRV_PROC_UNKONWN_INSTRUCTION = 20020
DRV_ILLEGAL_OP_CODE = 20021
DRV_KINETIC_TIME_NOT_MET = 20022
DRV_ACCUM_TIME_NOT_MET = 20023
DRV_NO_NEW_DATA = 20024
DRV_PCI_DMA_FAIL = 20025
DRV_SPOOLERROR = 20026
DRV_SPOOLSETUPERROR = 20027
DRV_FILESIZELIMITERROR = 20028
DRV_ERROR_FILESAVE = 20029

DRV_TEMPERATURE_CODES = 20033
DRV_TEMPERATURE_OFF = 20034
DRV_TEMPERATURE_NOT_STABILIZED = 20035
DRV_TEMPERATURE_STABILIZED = 20036
DRV_TEMPERATURE_NOT_REACHED = 20037
DRV_TEMPERATURE_OUT_RANGE = 20038
DRV_TEMPERATURE_NOT_SUPPORTED = 20039
DRV_TEMPERATURE_DRIFT = 20040

DRV_TEMP_CODES = 20033
DRV_TEMP_OFF = 20034
DRV_TEMP_NOT_STABILIZED = 20035
DRV_TEMP_STABILIZED = 20036
DRV_TEMP_NOT_REACHED = 20037
DRV_TEMP_OUT_RANGE = 20038
DRV_TEMP_NOT_SUPPORTED = 20039
DRV_TEMP_DRIFT = 20040

DRV_GENERAL_ERRORS = 20049
DRV_INVALID_AUX = 20050
DRV_COF_NOTLOADED = 20051
DRV_FPGAPROG = 20052
DRV_FLEXERROR = 20053
DRV_GPIBERROR = 20054
DRV_EEPROMVERSIONERROR = 20055

DRV_DATATYPE = 20064
DRV_DRIVER_ERRORS = 20065
DRV_P1INVALID = 20066
DRV_P2INVALID = 20067
DRV_P3INVALID = 20068
DRV_P4INVALID = 20069
DRV_INIERROR = 20070
DRV_COFERROR = 20071
DRV_ACQUIRING = 20072
DRV_IDLE = 20073
DRV_TEMPCYCLE = 20074
DRV_NOT_INITIALIZED = 20075
DRV_P5INVALID = 20076
DRV_P6INVALID = 20077
DRV_INVALID_MODE = 20078
DRV_INVALID_FILTER = 20079

DRV_I2CERRORS = 20080
DRV_I2CDEVNOTFOUND = 20081
DRV_I2CTIMEOUT = 20082
DRV_P7INVALID = 20083
DRV_P8INVALID = 20084
DRV_P9INVALID = 20085
DRV_P10INVALID = 20086

DRV_USBERROR = 20089
DRV_IOCERROR = 20090
DRV_VRMVERSIONERROR = 20091
DRV_USB_INTERRUPT_ENDPOINT_ERROR = 20093
DRV_RANDOM_TRACK_ERROR = 20094
DRV_INVALID_TRIGGER_MODE = 20095
DRV_LOAD_FIRMWARE_ERROR = 20096
DRV_DIVIDE_BY_ZERO_ERROR = 20097
DRV_INVALID_RINGEXPOSURES = 20098
DRV_BINNING_ERROR = 20099
DRV_INVALID_AMPLIFIER = 20100

DRV_ERROR_NOCAMERA = 20990
DRV_NOT_SUPPORTED = 20991
DRV_NOT_AVAILABLE = 20992

DRV_ERROR_MAP = 20115
DRV_ERROR_UNMAP = 20116
DRV_ERROR_MDL = 20117
DRV_ERROR_UNMDL = 20118
DRV_ERROR_BUFFSIZE = 20119
DRV_ERROR_NOHANDLE = 20121

DRV_GATING_NOT_AVAILABLE = 20130
DRV_FPGA_VOLTAGE_ERROR = 20131

DRV_OW_CMD_FAIL = 20150
DRV_OWMEMORY_BAD_ADDR = 20151
DRV_OWCMD_NOT_AVAILABLE = 20152
DRV_OW_NO_SLAVES = 20153
DRV_OW_NOT_INITIALIZED = 20154
DRV_OW_ERROR_SLAVE_NUM = 20155
DRV_MSTIMINGS_ERROR = 20156

AC_ACQMODE_SINGLE = 1
AC_ACQMODE_VIDEO = 2
AC_ACQMODE_ACCUMULATE = 4
AC_ACQMODE_KINETIC = 8
AC_ACQMODE_FRAMETRANSFER = 16
AC_ACQMODE_FASTKINETICS = 32
AC_ACQMODE_OVERLAP = 64

# Readout mode
AC_READMODE_FULLIMAGE = 1
AC_READMODE_SUBIMAGE = 2
AC_READMODE_SINGLETRACK = 4
AC_READMODE_FVB = 8
AC_READMODE_MULTITRACK = 16
AC_READMODE_RANDOMTRACK = 32
AC_READMODE_MULTITRACKSCAN = 64

AC_TRIGGERMODE_INTERNAL = 1
AC_TRIGGERMODE_EXTERNAL = 2
AC_TRIGGERMODE_EXTERNAL_FVB_EM = 4
AC_TRIGGERMODE_CONTINUOUS = 8
AC_TRIGGERMODE_EXTERNALSTART = 16
AC_TRIGGERMODE_EXTERNALEXPOSURE = 32
AC_TRIGGERMODE_INVERTED = 0x40

# = Deprecated = for = AC_TRIGGERMODE_EXTERNALEXPOSURE
AC_TRIGGERMODE_BULB = 32

AC_CAMERATYPE_PDA = 0
AC_CAMERATYPE_IXON = 1
AC_CAMERATYPE_ICCD = 2
AC_CAMERATYPE_EMCCD = 3
AC_CAMERATYPE_CCD = 4
AC_CAMERATYPE_ISTAR = 5
AC_CAMERATYPE_VIDEO = 6
AC_CAMERATYPE_IDUS = 7
AC_CAMERATYPE_NEWTON = 8
AC_CAMERATYPE_SURCAM = 9
AC_CAMERATYPE_USBICCD = 10
AC_CAMERATYPE_LUCA = 11
AC_CAMERATYPE_RESERVED = 12
AC_CAMERATYPE_IKON = 13
AC_CAMERATYPE_INGAAS = 14
AC_CAMERATYPE_IVAC = 15
AC_CAMERATYPE_UNPROGRAMMED = 16
AC_CAMERATYPE_CLARA = 17
AC_CAMERATYPE_USBISTAR = 18

AC_PIXELMODE_8BIT = 1
AC_PIXELMODE_14BIT = 2
AC_PIXELMODE_16BIT = 4
AC_PIXELMODE_32BIT = 8

AC_PIXELMODE_MONO = 0x000000
AC_PIXELMODE_RGB = 0x010000
AC_PIXELMODE_CMY = 0x020000

AC_SETFUNCTION_VREADOUT = 0x01
AC_SETFUNCTION_HREADOUT = 0x02
AC_SETFUNCTION_TEMPERATURE = 0x04
AC_SETFUNCTION_MCPGAIN = 0x08
AC_SETFUNCTION_EMCCDGAIN = 0x10
AC_SETFUNCTION_BASELINECLAMP = 0x20
AC_SETFUNCTION_VSAMPLITUDE = 0x40
AC_SETFUNCTION_HIGHCAPACITY = 0x80
AC_SETFUNCTION_BASELINEOFFSET = 0x0100
AC_SETFUNCTION_PREAMPGAIN = 0x0200
AC_SETFUNCTION_CROPMODE = 0x0400
AC_SETFUNCTION_DMAPARAMETERS = 0x0800
AC_SETFUNCTION_HORIZONTALBIN = 0x1000
AC_SETFUNCTION_MULTITRACKHRANGE = 0x2000
AC_SETFUNCTION_RANDOMTRACKNOGAPS = 0x4000
AC_SETFUNCTION_EMADVANCED = 0x8000
AC_SETFUNCTION_GATEMODE = 0x010000
AC_SETFUNCTION_DDGTIMES = 0x020000
AC_SETFUNCTION_IOC = 0x040000
AC_SETFUNCTION_INTELLIGATE = 0x080000
AC_SETFUNCTION_INSERTION_DELAY = 0x100000
AC_SETFUNCTION_GATESTEP = 0x200000

# = Deprecated = for = AC_SETFUNCTION_MCPGAIN
AC_SETFUNCTION_GAIN = 8
AC_SETFUNCTION_ICCDGAIN = 8

AC_GETFUNCTION_TEMPERATURE = 0x01
AC_GETFUNCTION_TARGETTEMPERATURE = 0x02
AC_GETFUNCTION_TEMPERATURERANGE = 0x04
AC_GETFUNCTION_DETECTORSIZE = 0x08
AC_GETFUNCTION_MCPGAIN = 0x10
AC_GETFUNCTION_EMCCDGAIN = 0x20
AC_GETFUNCTION_HVFLAG = 0x40
AC_GETFUNCTION_GATEMODE = 0x80
AC_GETFUNCTION_DDGTIMES = 0x0100
AC_GETFUNCTION_IOC = 0x0200
AC_GETFUNCTION_INTELLIGATE = 0x0400
AC_GETFUNCTION_INSERTION_DELAY = 0x0800
AC_GETFUNCTION_GATESTEP = 0x1000
AC_GETFUNCTION_PHOSPHORSTATUS = 0x2000
AC_GETFUNCTION_MCPGAINTABLE = 0x4000

# = Deprecated = for = AC_GETFUNCTION_MCPGAIN
AC_GETFUNCTION_GAIN = 0x10
AC_GETFUNCTION_ICCDGAIN = 0x10

AC_FEATURES_POLLING = 1
AC_FEATURES_EVENTS = 2
AC_FEATURES_SPOOLING = 4
AC_FEATURES_SHUTTER = 8
AC_FEATURES_SHUTTEREX = 16
AC_FEATURES_EXTERNAL_I2C = 32
AC_FEATURES_SATURATIONEVENT = 64
AC_FEATURES_FANCONTROL = 128
AC_FEATURES_MIDFANCONTROL = 256
AC_FEATURES_TEMPERATUREDURINGACQUISITION = 512
AC_FEATURES_KEEPCLEANCONTROL = 1024
AC_FEATURES_DDGLITE = 0x0800
AC_FEATURES_FTEXTERNALEXPOSURE = 0x1000
AC_FEATURES_KINETICEXTERNALEXPOSURE = 0x2000
AC_FEATURES_DACCONTROL = 0x4000
AC_FEATURES_METADATA = 0x8000
AC_FEATURES_IOCONTROL = 0x10000
AC_FEATURES_PHOTONCOUNTING = 0x20000

AC_EMGAIN_8BIT = 1
AC_EMGAIN_12BIT = 2
AC_EMGAIN_LINEAR12 = 4
AC_EMGAIN_REAL12 = 8

def initialize(dir='c:/program files/andor andor/drivers/'):
    global andor
    andor = windll.atmcd32d
    ret = andor.Initialize(dir)
    return ret

def get_detector():
    xpix, ypix = c_int32(0), c_int32(0)
    ret = andor.GetDetector(byref(xpix), byref(ypix))
    return xpix.value, ypix.value

def get_temperature_range():
    temprangemin = c_int32(0)
    temprangemax = c_int32(0)
    ret = andor.GetTemperatureRange(byref(temprangemin),byref(temprangemax))
    return temprangemin.value, temprangemax.value

def get_temperature():
    temp = c_int32(0)
    ret = andor.GetTemperature(byref(temp))
    return temp.value

def set_target_temperature(temp, wait=False):
    ctemp = c_int(temp)
    ret = andor.SetTemperature(ctemp)
    return ret

def is_cooler_on():
    statuscooler = c_int32(0)
    ret = andor.IsCoolerOn(byref(statuscooler))
    return statuscooler.value

def set_cooler_on(on=True):
    if on:
        ret = andor.CoolerON()
    else:
        ret = andor.CoolerOFF()
    return ret

def set_coolor_off():
    return set_cooler_on(False)

def set_exposure_time(exposuretime):
    ret = andor.SetExposureTime(c_float(exposuretime))
    return ret

def start_acquisition():
    ret = andor.StartAcquisition()
    return ret

def get_status():
    status = c_int32(0)
    ret = andor.GetStatus(byref(status))
    return status.value

def wait_idle(delay=30):
    start = time.time()
    while (time.time() - start) < delay:
        if get_status() == DRV_IDLE:
            return True
        time.sleep(0.5)
    return False

def get_acquired_data(bufsize=1024):
    data = np.zeros(bufsize, dtype=np.int32)
    ret = andor.GetAcquiredData(data.ctypes.data, bufsize)
    return data

def get_spectrum():
    xpix, ypix = get_detector()
    start_acquisition()
    while get_status() == DRV_ACQUIRING:
        time.sleep(0.1)
    time.sleep(0.2)
    return get_acquired_data(xpix)

def get_spectrum_adv(background=None, ntries=3, thresh=0.15):
    '''
    Get a spectrum from the Andor. Subtracts background and tries to
    detect 'bad' pixels, in case of which a new spectrum will be
    taken (up to ntries times).
    '''
    for i in range(ntries):
        spec = get_spectrum()
        if background is not None:
            spec -= background

        maxval = np.max(spec)
        if maxval < 100:
            return spec

        minval = maxval * thresh
        maxpos = np.argmax(spec)

        # If any of the neighbouring points is above the threshold it's ok.
        if (maxpos == 0 or spec[maxpos-1] >= minval) or \
            (maxpos == len(spec) - 1 or spec[maxpos+1] >= minval):
            return spec

        print 'Bad pixel detected!'

    print 'Warning: returning spectrum with possibly bad pixel'
    for i in range(maxpos-5,maxpos+5):
        print 'pos %d = %d' % (i, spec[i])

    return spec


def get_temperature():
    temp = c_int32(0)
    ret = andor.GetTemperature(byref(temp))
    return temp.value

def shutdown():
    ret = andor.ShutDown()

def set_read_mode(mode):
    '''
    mode:
        0: Full Vertical Binning
        1: Multi-track
        2: Ramdom track
        3: Single track
        4: Full resolution
    '''
    romode = c_int32(mode)
    ret = andor.SetReadMode(romode)
    return ret

def get_read_mode():
    romode = c_int32(0)
    ret = andor.GetReadMode(byref(romode))
    return romode.value

# SetShutter
# SetTriggerMode
# SetAccumulationCycletime
# SetNumberAccumulations
# SetNumberKinetics
# SetKineticCycletime
# GetAcquisitiontimings
# SetHSSpeed
# SetVSSpeed
