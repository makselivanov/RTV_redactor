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

InnerPoint InnerPoint::operator+(const InnerPoint &other) const {
    InnerPoint buffer(*this);
    buffer += other;
    return std::move(buffer);
}

InnerPoint& InnerPoint::operator-=(const InnerPoint &other) {
    px -= other.px;
    py -= other.py;
    return *this;
}

InnerPoint InnerPoint::operator-(const InnerPoint &other) const {
    InnerPoint buffer(*this);
    buffer -= other;
    return std::move(buffer);
}

MetricDist InnerPoint::dp(const InnerPoint &other) const {
    return px * other.px + py * other.py;
}

MetricDist InnerPoint::cp(const InnerPoint &other) const {
    return px * other.py - py * other.px;
}

Figure::Figure() : scale_(1), angle_(0), center_(0, 0) {}

void Figure::extend(MetricDist scale) {
    scale_ *= scale;
}

void Figure::move(const InnerPoint &position) {
    center_ += position;
}

void Figure::moveTo(const InnerPoint &position) {
    center_ = position;
}

void Figure::turn(Angular angle) {
    angle_ += angle;
    if (angle_ > 2 * PI || angle_ < 0)
        angle_ = std::fmod(angle_, 2 * PI);
}