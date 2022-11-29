from sensor.exception import SensorException
import sys

def test_exception():
    try:
        x=1/0
    except Exception as e:
        raise SensorException(e,sys)

if __name__ =="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)