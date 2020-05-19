#ifndef RTV_REDACTOR_FIGURE_H
#define RTV_REDACTOR_FIGURE_H

#include <vector>

typedef double Coordinate;
typedef double MetricDist;
typedef double Angular;
const Coordinate EPS = 0.04;
const Angular PI = 3.14159265358979323;

class InnerPoint {
    Coordinate px;
    Coordinate py;
public:
    InnerPoint(Coordinate x, Coordinate y);
    InnerPoint() = default;
    InnerPoint(const InnerPoint &other) = default;

    InnerPoint &operator=(const InnerPoint &other) = default;
    InnerPoint &operator=(InnerPoint &&other) = default;

    Coordinate getX() const;
    void setX(Coordinate x);
    Coordinate getY() const;
    void setY(Coordinate y);

    bool operator==(const InnerPoint &other) const;
    bool operator!=(const InnerPoint &other) const;

    InnerPoint operator+(const InnerPoint &other) const;
    InnerPoint &operator+=(const InnerPoint &other);
    InnerPoint operator-(const InnerPoint &other) const;
    InnerPoint &operator-=(const InnerPoint &other);

    MetricDist hypot() const;
    MetricDist dp(const InnerPoint &other) const; //dot product
    MetricDist cp(const InnerPoint &other) const; //cross product
};

class PointList {
    std::vector<InnerPoint> points;
public:
};

class Figure {
    InnerPoint center_;
    Angular angle_;
    MetricDist scale_;
public:
    Figure();
    virtual ~Figure() = default;
    void extend(MetricDist scale);
    void move(const InnerPoint& position);
    void moveTo(const InnerPoint& position);
    void turn(Angular angle);
};

#endif //RTV_REDACTOR_FIGURE_H
