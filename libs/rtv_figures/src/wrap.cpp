#include "figure.h"
#include <boost/python.hpp>

BOOST_PYTHON_MODULE(rtv_figures) {
    using namespace boost::python;
    class_<InnerPoint>("InnerPoint")
            .def(init<Coordinate, Coordinate>(args("x", "y")))
            .def(init<InnerPoint>(args("other")))
            .add_property("x", &InnerPoint::getX, &InnerPoint::setX)
            .add_property("y", &InnerPoint::getY, &InnerPoint::setY)
            .def("__eq__", &InnerPoint::operator==)
            .def("__ne__", &InnerPoint::operator!=)
            .def("hypot", &InnerPoint::hypot)
            .def("dp", &InnerPoint::dp)
            .def("cp", &InnerPoint::cp);
            /*.def("__add__", &InnerPoint::operator+)
            .def("__iadd__", &InnerPoint::operator+=)
            .def("__sub__", &InnerPoint::operator-)
            .def("__isub__", &InnerPoint::operator-=);*/
}