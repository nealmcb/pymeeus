# -*- coding: utf-8 -*-


# PyMeeus: Python module implementing astronomical algorithms.
# Copyright (C) 2018  Dagoberto Salazar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pymeeus.base import TOL
from pymeeus.Saturn import Saturn
from pymeeus.Epoch import Epoch


# Saturn class

def test_saturn_geometric_heliocentric_position():
    """Tests the geometric_heliocentric_position() method of Saturn class"""

    epoch = Epoch(2018, 10, 27.0)
    lon, lat, r = Saturn.geometric_heliocentric_position(epoch)

    assert abs(round(lon.to_positive(), 4) - 279.5108) < TOL, \
        "ERROR: 1st geometric_heliocentric_position() test doesn't match"

    assert abs(round(lat, 4) - 0.6141) < TOL, \
        "ERROR: 2nd geometric_heliocentric_position() test doesn't match"

    assert abs(round(r, 5) - 10.06266) < TOL, \
        "ERROR: 3rd geometric_heliocentric_position() test doesn't match"


def test_saturn_orbital_elements_mean_equinox():
    """Tests the orbital_elements_mean_equinox() method of Saturn class"""

    epoch = Epoch(2065, 6, 24.0)
    l, a, e, i, ome, arg = Saturn.orbital_elements_mean_equinox(epoch)

    assert abs(round(l, 6) - 131.196871) < TOL, \
        "ERROR: 1st orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(a, 8) - 9.55490779) < TOL, \
        "ERROR: 2nd orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(e, 7) - 0.0553209) < TOL, \
        "ERROR: 3rd orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(i, 6) - 2.486426) < TOL, \
        "ERROR: 4th orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(ome, 5) - 114.23974) < TOL, \
        "ERROR: 5th orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(arg, 6) - (-19.896331)) < TOL, \
        "ERROR: 6th orbital_elements_mean_equinox() test doesn't match"


def test_saturn_orbital_elements_j2000():
    """Tests the orbital_elements_j2000() method of Saturn class"""

    epoch = Epoch(2065, 6, 24.0)
    l, a, e, i, ome, arg = Saturn.orbital_elements_j2000(epoch)

    assert abs(round(l, 6) - 130.28188) < TOL, \
        "ERROR: 1st orbital_elements_j2000() test doesn't match"

    assert abs(round(a, 8) - 9.55490779) < TOL, \
        "ERROR: 2nd orbital_elements_j2000() test doesn't match"

    assert abs(round(e, 7) - 0.0553209) < TOL, \
        "ERROR: 3rd orbital_elements_j2000() test doesn't match"

    assert abs(round(i, 6) - 2.490529) < TOL, \
        "ERROR: 4th orbital_elements_j2000() test doesn't match"

    assert abs(round(ome, 5) - 113.49736) < TOL, \
        "ERROR: 5th orbital_elements_j2000() test doesn't match"

    assert abs(round(arg, 6) - (-20.068943)) < TOL, \
        "ERROR: 6th orbital_elements_j2000() test doesn't match"


def test_saturn_geocentric_position():
    """Tests the geocentric_position() method of Saturn class"""

    epoch = Epoch(1992, 12, 20.0)
    ra, dec, elon = Saturn.geocentric_position(epoch)

    assert ra.ra_str(n_dec=1) == "21h 11' 41.8''", \
        "ERROR: 1st geocentric_position() test doesn't match"

    assert dec.dms_str(n_dec=1) == "-17d 15' 40.8''", \
        "ERROR: 2nd geocentric_position() test doesn't match"

    assert elon.dms_str(n_dec=1) == "46d 51' 47.7''", \
        "ERROR: 3rd geocentric_position() test doesn't match"


def test_saturn_conjunction():
    """Tests the conjunction() method of Saturn class"""

    epoch = Epoch(2125, 6, 1.0)
    conjunction = Saturn.conjunction(epoch)
    y, m, d = conjunction.get_date()

    assert abs(round(y, 0) - 2125) < TOL, \
        "ERROR: 1st conjunction() test doesn't match"

    assert abs(round(m, 0) - 8) < TOL, \
        "ERROR: 2nd conjunction() test doesn't match"

    assert abs(round(d, 4) - 26.4035) < TOL, \
        "ERROR: 3rd conjunction() test doesn't match"


def test_saturn_opposition():
    """Tests the opposition() method of Saturn class"""

    epoch = Epoch(-6, 9, 1.0)
    oppo = Saturn.opposition(epoch)
    y, m, d = oppo.get_date()

    assert abs(round(y, 0) - (-6)) < TOL, \
        "ERROR: 1st opposition() test doesn't match"

    assert abs(round(m, 0) - 9) < TOL, \
        "ERROR: 2nd opposition() test doesn't match"

    assert abs(round(d, 4) - 14.3709) < TOL, \
        "ERROR: 3rd opposition() test doesn't match"


def test_saturn_station_longitude_1():
    """Tests the station_longitude_1() method of Saturn class"""

    epoch = Epoch(2018, 11, 1.0)
    sta1 = Saturn.station_longitude_1(epoch)
    y, m, d = sta1.get_date()

    assert abs(round(y, 0) - 2018) < TOL, \
        "ERROR: 1st station_longitude_1() test doesn't match"

    assert abs(round(m, 0) - 4) < TOL, \
        "ERROR: 2nd station_longitude_1() test doesn't match"

    assert abs(round(d, 4) - 17.9433) < TOL, \
        "ERROR: 3rd station_longitude_1() test doesn't match"


def test_saturn_station_longitude_2():
    """Tests the station_longitude_2() method of Saturn class"""

    epoch = Epoch(2018, 11, 1.0)
    sta2 = Saturn.station_longitude_2(epoch)
    y, m, d = sta2.get_date()

    assert abs(round(y, 0) - 2018) < TOL, \
        "ERROR: 1st station_longitude_2() test doesn't match"

    assert abs(round(m, 0) - 9) < TOL, \
        "ERROR: 2nd station_longitude_2() test doesn't match"

    assert abs(round(d, 4) - 6.4175) < TOL, \
        "ERROR: 3rd station_longitude_2() test doesn't match"
