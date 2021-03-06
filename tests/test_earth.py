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
from pymeeus.Earth import Earth, IAU76
from pymeeus.Angle import Angle
from pymeeus.Epoch import Epoch


# Earth class

def test_earth_constructor():
    """Tests the constructor of Earth class"""

    a = Earth()
    assert abs(a._ellip._a - 6378137.0) < TOL, \
        "ERROR: 1st constructor test, 'a' value doesn't match"

    assert abs(a._ellip._f - (1.0/298.257223563)) < TOL, \
        "ERROR: 2nd constructor test, 'f' value doesn't match"

    assert abs(a._ellip._omega - 7292115e-11) < TOL, \
        "ERROR: 3rd constructor test, 'omega' value doesn't match"

    a = Earth(ellipsoid=IAU76)
    assert abs(a._ellip._a - 6378140.0) < TOL, \
        "ERROR: 4th constructor test, 'a' value doesn't match"

    assert abs(a._ellip._f - (1.0/298.257)) < TOL, \
        "ERROR: 5th constructor test, 'f' value doesn't match"

    assert abs(a._ellip._omega - 7.292114992e-5) < TOL, \
        "ERROR: 6th constructor test, 'omega' value doesn't match"


def test_earth_rho():
    """Tests the rho() method of Earth class"""

    a = Earth()
    assert abs(a.rho(0.0) - 1.0) < TOL, \
        "ERROR: 1st rho() test, output doesn't match"


def test_earth_rho_sinphi():
    """Tests the rho_sinphi() method of Earth class"""

    lat = Angle(33, 21, 22.0)
    e = Earth(ellipsoid=IAU76)
    assert abs(round(e.rho_sinphi(lat, 1706), 6) - 0.546861) < TOL, \
        "ERROR: 1st rho_sinphi() test, output doesn't match"


def test_earth_rho_cosphi():
    """Tests the rho_cosphi() method of Earth class"""

    lat = Angle(33, 21, 22.0)
    e = Earth(ellipsoid=IAU76)
    assert abs(round(e.rho_cosphi(lat, 1706), 6) - 0.836339) < TOL, \
        "ERROR: 1st rho_cosphi() test, output doesn't match"


def test_earth_rp():
    """Tests the rp() method of Earth class"""

    e = Earth(ellipsoid=IAU76)
    assert abs(round(e.rp(42.0), 1) - 4747001.2) < TOL, \
        "ERROR: 1st rp() test, output doesn't match"


def test_earth_rm():
    """Tests the rm() method of Earth class"""

    e = Earth(ellipsoid=IAU76)
    assert abs(round(e.rm(42.0), 1) - 6364033.3) < TOL, \
        "ERROR: 1st rm() test, output doesn't match"


def test_earth_linear_velocity():
    """Tests the linear_velocity() method of Earth class"""

    e = Earth(ellipsoid=IAU76)
    assert abs(round(e.linear_velocity(42.0), 2) - 346.16) < TOL, \
        "ERROR: 1st linear_velocity() test, output doesn't match"


def test_earth_distance():
    """Tests the distance() method of Earth class"""

    e = Earth(ellipsoid=IAU76)
    lon1 = Angle(-2, 20, 14.0)
    lat1 = Angle(48, 50, 11.0)
    lon2 = Angle(77, 3, 56.0)
    lat2 = Angle(38, 55, 17.0)
    dist, error = e.distance(lon1, lat1, lon2, lat2)

    assert abs(round(dist, 0) - 6181628.0) < TOL, \
        "ERROR: 1st distance() test, output doesn't match"

    assert abs(round(error, 0) - 69.0) < TOL, \
        "ERROR: 2nd distance() test, output doesn't match"

    lon1 = Angle(-2.09)
    lat1 = Angle(41.3)
    lon2 = Angle(73.99)
    lat2 = Angle(40.75)
    dist, error = e.distance(lon1, lat1, lon2, lat2)

    assert abs(round(dist, 0) - 6176760.0) < TOL, \
        "ERROR: 3rd distance() test, output doesn't match"

    assert abs(round(error, 0) - 69.0) < TOL, \
        "ERROR: 4th distance() test, output doesn't match"


def test_earth_geometric_heliocentric_position():
    """Tests the geometric_heliocentric_position() method of Earth class"""

    epoch = Epoch(1992, 10, 13.0)
    lon, lat, r = Earth.geometric_heliocentric_position(epoch)

    assert abs(round(lon.to_positive(), 6) - 19.907272) < TOL, \
        "ERROR: 1st geometric_heliocentric_position() test doesn't match"

    assert lat.dms_str(n_dec=3) == "-0.721''", \
        "ERROR: 2nd geometric_heliocentric_position() test doesn't match"

    assert abs(round(r, 8) - 0.99760852) < TOL, \
        "ERROR: 3rd geometric_heliocentric_position() test doesn't match"


def test_earth_apparent_heliocentric_position():
    """Tests the apparent_heliocentric_position() method of Earth class"""

    epoch = Epoch(1992, 10, 13.0)
    lon, lat, r = Earth.apparent_heliocentric_position(epoch)

    assert abs(round(lon.to_positive(), 6) - 19.905986) < TOL, \
        "ERROR: 1st apparent_heliocentric_position() test doesn't match"

    assert lat.dms_str(n_dec=3) == "-0.721''", \
        "ERROR: 2nd apparent_heliocentric_position() test doesn't match"

    assert abs(round(r, 8) - 0.99760852) < TOL, \
        "ERROR: 3rd apparent_heliocentric_position() test doesn't match"


def test_earth_orbital_elements_mean_equinox():
    """Tests the orbital_elements_mean_equinox() method of Earth class"""

    epoch = Epoch(2065, 6, 24.0)
    l, a, e, i, ome, arg = Earth.orbital_elements_mean_equinox(epoch)

    assert abs(round(l, 6) - 272.716028) < TOL, \
        "ERROR: 1st orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(a, 8) - 1.00000102) < TOL, \
        "ERROR: 2nd orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(e, 7) - 0.0166811) < TOL, \
        "ERROR: 3rd orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(i, 6) - 0.0) < TOL, \
        "ERROR: 4th orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(ome, 5) - 174.71534) < TOL, \
        "ERROR: 5th orbital_elements_mean_equinox() test doesn't match"

    assert abs(round(arg, 6) - (-70.651889)) < TOL, \
        "ERROR: 6th orbital_elements_mean_equinox() test doesn't match"


def test_earth_orbital_elements_j2000():
    """Tests the orbital_elements_j2000() method of Earth class"""

    epoch = Epoch(2065, 6, 24.0)
    l, a, e, i, ome, arg = Earth.orbital_elements_j2000(epoch)

    assert abs(round(l, 6) - 271.801199) < TOL, \
        "ERROR: 1st orbital_elements_j2000() test doesn't match"

    assert abs(round(a, 8) - 1.00000102) < TOL, \
        "ERROR: 2nd orbital_elements_j2000() test doesn't match"

    assert abs(round(e, 7) - 0.0166811) < TOL, \
        "ERROR: 3rd orbital_elements_j2000() test doesn't match"

    assert abs(round(i, 6) - 0.008544) < TOL, \
        "ERROR: 4th orbital_elements_j2000() test doesn't match"

    assert abs(round(ome, 5) - 174.71534) < TOL, \
        "ERROR: 5th orbital_elements_j2000() test doesn't match"

    assert abs(round(arg, 6) - (-71.566717)) < TOL, \
        "ERROR: 6th orbital_elements_j2000() test doesn't match"
