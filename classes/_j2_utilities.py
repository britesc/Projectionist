#!/usr/bin/env python3
# coding: utf-8
from time import time


class J2_Utilities():
    """ A Class containing Utilities """

    def __init__(self) -> None:
        """ The __init__ Function """
        pass

    def __str__(self) -> str:
        """ The __str__ Function """
        return "J2 Utilities"

    def __repr__(self) -> str:
        """ The __repr__ Function """
        return "J2_Utilities"

    def getVersion(self) -> str:
        """ The Version String of this Class """
        self.Version = "1.0.0"
        return self.Version

    def j2Sleep(self, secs) -> None:
        """ An Alternative to Python Sleep """
        init_time = time()
        while time() < init_time+secs:
            pass
