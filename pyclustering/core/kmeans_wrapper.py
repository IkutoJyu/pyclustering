"""!

@brief CCORE Wrapper for K-Means algorithm.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2017
@copyright GNU Public License

@cond GNU_PUBLIC_LICENSE
    PyClustering is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    PyClustering is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endcond

"""


from ctypes import cdll, c_double, POINTER;

from pyclustering.core.wrapper import PATH_DLL_CCORE_64, create_pointer_data, extract_pyclustering_package, pyclustering_package;


def kmeans(sample, centers, tolerance):
    pointer_data = create_pointer_data(sample);
    pointer_centers = create_pointer_data(centers);
    
    ccore = cdll.LoadLibrary(PATH_DLL_CCORE_64);
    
    ccore.kmeans_algorithm.restype = POINTER(pyclustering_package);
    package = ccore.kmeans_algorithm(pointer_data, pointer_centers, c_double(tolerance));
    
    result = extract_pyclustering_package(package);
    ccore.free_pyclustering_package(package);
    
    return result;