Points[] p;
int pNum = 0;
int pCount = 30;

void setup() {
  size(400, 400);
  pixelDensity(1);
  p = new Points[pCount];
  for (int i = 0; i < p.length; i++) {
    p[i] = new Points();
  }
}

void draw() {
  background(0);


  loadPixels();
  weightMap();
  updatePixels();
}

void weightMap() {
  float r = 0;
  color c;
  
  //go through all pixels
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      int loc = x + y * width;


      r = norm(idw(x, y), 0, 255);
      
      //screen blend mode 
      float scr = ((1-r))*255;
      
      // set the color of the pixels
      r = scr;
      c = color(r, r, r);
      pixels[loc] = c;
    }
  }
}

// inverse distance weighted file
float idw(float px, float py) {
  float wSum = 0;
  float vSum = 0;

  //rate at which values decay
  float decay = 0.5;

  for (int i = 0; i < p.length; i++) {

    float d = dist(px, py, p[i].x, p[i].y);
    float w = 1 / pow(d, decay);

    // setting the center of the point to white
    if (d < 1) return 255 - p[i].val;

    // sum of the values times their weights
    vSum += p[i].val*w;
    
    // sum of the weights
    wSum += w;
  }
  return 255-(vSum / wSum);
}



void mouseClicked() {
  //Addin a new Point
  p[pNum].plot(mouseX, mouseY);
  pNum++;
  if (pNum >= pCount) {
    pNum = 0;
  }
}
