#ifndef RTV_REDACTOR_FIGURE_H
#define RTV_REDACTOR_FIGURE_H

class Figure;
class Point : public Figure;

class Figure {
public:
    explicit Figure();
    virtual ~Figure();
    virtual void scale(double scale) = 0;
    virtual void move(const Point& position) = 0;
    virtual void turn(double angle) = 0;
};

class Point {
private:
    double x, y;
public:
    Point(double x, double y);
    double getX();
    double getY();
    double setX();
    double setY();
};

#endif //RTV_REDACTOR_FIGURE_H
