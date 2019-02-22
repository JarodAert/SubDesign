tubeD=130; tubeT=20; tubeH=300;

module MakePlug(D, T, RodD, RodL){
    cylinder(d=D, h=T);
    cylinder(d=RodD, h=RodL+T);
}

module MakeMainTube(tubeD, tubeT, tubeH){
    // Main Tube
    translate([0,0,2])
    difference(){
        cylinder(d=tubeD+tubeT, h=tubeH);
        translate([0,0,-1]) cylinder(d=tubeD, h=tubeH*1.1);
        translate([-tubeD-tubeT, 40, 50]) cube([tubeH, tubeD+tubeT, tubeH]);
    }
}

module MakeEndCap(){
    // End Cap
    difference(){
        cylinder(d=170, h=40);
        translate([0,0,20])
        cylinder(d=151, h=30);
    }   
}

module MakeRodHolder(){
    // Thing inside to hold the plug rod
    translate([0, 0, 175]) 
    difference(){
        cube([130, 50, 5], center=true);
        translate([0,0,-5])
        cylinder(d=11, h=30);
    } 
}

function timePos()=-320*pow($t-0.5,2)+80;

rotate([90,0,0]){
    MakeMainTube(tubeD, tubeT, tubeH);
    MakeEndCap();
    MakeRodHolder();
    // Plug that controls the accent and decent
    translate([0,0,300-timePos()]) rotate([180,0,0])
    color([1,0.41,0.38]) MakePlug(129, 30, 10, 125);
    // Stepper Motor
    translate([40,0,120]) import("./../Parts/Motor_NEMA17.stl");

    color([0.38, 1, 0.38]) translate([0,0,30]) cube([80, 80, 50], center=true);
}