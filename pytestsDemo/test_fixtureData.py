import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("Data")
class TestProfile(BaseClass):
    def test_ProfileDetails(self,Data):
        log= self.getLogger()
        log.info(Data[0])
        log.info(Data[1])
        print(Data[0])
        print(Data[1])
