

def hms_to_degrees(hours, minutes, seconds):
    minutes_h = minutes / 60
    secs_h = seconds / 3600
    degrees = (hours + minutes_h + secs_h) * 15
    return degrees


def dec_to_degrees(degrees, arcmin, arcsec):
    if "-" in str(degrees):
        sign = -1
    else:
        sign = 1

    degrees = float(degrees)

    arcmin_deg = arcmin / 60
    arcsec_deg = arcsec / 3600
    degrees_converted = (abs(degrees) + arcmin_deg + arcsec_deg) * sign
    return degrees_converted

if __name__ == '__main__':
    result = hms_to_degrees(17, 57, 48.498)
    print(f"hms to degrees = {result} degrees")
    result_2 = dec_to_degrees("-0", 30, 0)
    print(f"dec to degrees = {result_2} degrees")
