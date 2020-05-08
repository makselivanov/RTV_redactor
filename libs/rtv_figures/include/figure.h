#ifndef RTV_REDACTOR_FIGURE_H
#define RTV_REDACTOR_FIGURE_H

#include <vector>

typedef double Coordinate;
typedef double MetricDist;
typedef double Angular;
const Coordinate EPS = 0.04;

class InnerPoint {
    Coordinate x;
    Coordinate y;
public:
    InnerPoint(Coordinate x, Coordinate y);
    InnerPoint();
    Coordinate getX() const noexcept;
    void setX(Coordinate x) noexcept;
    Coordinate getY() const noexcept;
    void setY(Coordinate y) noexcept;
    bool operator==(const InnerPoint& other) const noexcept;
    bool operator!=(const InnerPoint& other) const noexcept;
    MetricDist hypot() const noexcept;
    InnerPoint operator+(const InnerPoint& other) const noexcept;
    InnerPoint operator+=(const InnerPoint& other) noexcept;
    InnerPoint operator-(const InnerPoint& other) const noexcept;
    InnerPoint operator-=(const InnerPoint& other) noexcept;
    MetricDist dp(const InnerPoint& other) const noexcept; //dot product
    MetricDist cp(const InnerPoint& other) const noexcept; //cross product
};

class PointList {
    std::vector<InnerPoint> points;
public:
};

class Figure {
    InnerPoint center;
    Angular angle;
    MetricDist scale;
public:
    Figure();
    virtual ~Figure();
    void extend(MetricDist scale);
    void move(const InnerPoint& position);
    void moveTo(const InnerPoint& position);
    void turn(Angular angle);
};

#endif //RTV_REDACTOR_FIGURE_H
