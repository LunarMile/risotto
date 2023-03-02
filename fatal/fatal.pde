Table data;

PImage map;
PImage mapB;
String url = "https://api.mapbox.com/styles/v1/emilio-suarez/clcrrzrqf002a15oewtqtzhdu/static/-97.563122,38.068852,3.50/1024x1024?access_token=pk.eyJ1IjoiZW1pbGlvLXN1YXJleiIsImEiOiJjbGNycnc3cXQwYnQyM29wY2xlMGZiamIyIn0.ZKhYT5pyyRoo_wNXMF4Iiw";


float cX, cY;
float clon = -97.563122;
float clat = 38.068852;
float zoom = 3.5;

void setup() {
  size(1024, 1024, P2D);
  map = loadImage(url, "png");

  data = loadTable("data/fatalData.csv");

  cX = mercX(clon);
  cY = mercY(clat);

  image(map, 0, 0);
}


void draw() {
  translate(width/2, height/2);
  fill(255);
  noStroke();

  for (int i = 0; i < data.getRowCount()-1; i++) {
    TableRow dataRow = data.getRow(i+1);
    float lat = dataRow.getFloat(15);
    float lon = dataRow.getFloat(16);

    float fy = mercY(lat);
    float fx = mercX(lon);

    println(fx + ",  " + fy);
    ellipse(fx, fy, 2, 2);
  }
  saveFrame("result1.png");
  noLoop();
  
}

// Longitude to x  (WEBMercator)
float mercX(float lon) {
  lon = radians(lon);
  float a = (256 / PI) * pow(2, zoom);
  float b = lon + PI;
  return (a * b) - cX;
}


// Lattitude to y  (WEBMercator)
float mercY(float lat) {
  lat = radians(lat);
  float a = (256 / PI) * pow(2, zoom);
  float b = tan(PI / 4 + lat / 2);
  float c = PI - log(b);
  return (a * c) - cY;
}
