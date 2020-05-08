#include "figure.h"
#include <cmath>

InnerPoint::InnerPoint(Coordinate x, Coordinate y): px(x), py(y) {}

Coordinate InnerPoint::getX() const {
    return px;
}

void InnerPoint::setX(Coordinate x) {
    px = x;
}

Coordinate InnerPoint::getY() const {
    return py;
}

void InnerPoint::setY(Coordinate y) {
    py = y;
}

bool InnerPoint::operator==(const InnerPoint& other) const {
    return abs(px - other.px) < EPS && abs(py - other.py) < EPS;
}

bool InnerPoint::operator!=(const InnerPoint& other) const {
    return abs(px - other.px) > EPS || abs(py - other.py) > EPS;
}

MetricDist InnerPoint::hypot() const {
    return sqrt(px * px + py * py);
}

InnerPoint& InnerPoint::operator+=(const InnerPoint &other) {
    px += other.px;
    py += other.py;
    return *this;
}

InnerPoint&& InnerPoint::operator+(const InnerPoint &other) const {
    InnerPoint buffer(*this);
    buffer += other;
    return buffer;
}

InnerPoint& InnerPoint::operator-=(const InnerPoint &other) {
    px -= other.px;
    py -= other.py;
    return *this;
}

InnerPoint&& InnerPoint::operator-(const InnerPoint &other) const {
    InnerPoint buffer(*this);
    buffer -= other;
    return buffer;
}

MetricDist InnerPoint::dp(const InnerPoint &other) const {
    return px * other.px + py * other.py;
}

MetricDist InnerPoint::cp(const InnerPoint &other) const {
    return px * other.py - py * other.px;
}