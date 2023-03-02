Table data;
int maxDate = 0;

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

  noStroke();
  textSize(32);

  TableRow readRow = data.getRow(((data.getRowCount()-1) - frameCount) % (data.getRowCount()-1));
  String date = readRow.getString(8);
  fill(0);
  rect(10 -width/2, 30 - height/2, 170, 40);
  fill(255);
  text(date, 20 - width/2, 60 - height/2);
  datePoints(date);
}


void datePoints(String date) {

  if (dateID(date) > maxDate) {
    maxDate = dateID(date);
    for (TableRow loadRow : data.findRows(date, 8)) {
      float lat = loadRow.getFloat(15);
      float lon = loadRow.getFloat(16);

      float fy = mercY(lat);
      float fx = mercX(lon);

      println(fx + ",  " + fy + ",  " + dateID(date));

      ellipse(fx, fy, 2, 2);
    }
  }
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


int dateID(String date) {
  String[] split = splitTokens(date, "/");
  int dd = int(split[1]);
  int mm = int(split[0]) * 100;
  int yyyy = int(split[2]) * 10000;

  return yyyy + mm + dd;
}
