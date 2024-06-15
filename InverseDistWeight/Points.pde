class Points {
  float x;
  float y;
  float r = 5;
  float val = 0;

  boolean on = false;

  void plot(float x_, float y_) {
    x = x_;
    y = y_;
        val = 255;
    on = true;

  }
  void display() {
    if (on == true) {
      fill(255);
      noStroke();
      ellipse(x, y, r, r);
    }
  }
}
