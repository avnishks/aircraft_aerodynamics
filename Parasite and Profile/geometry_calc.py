ref_area = 100
taper_ratio = 0.3333
aspect_ratio = 10


wetted_area = ref_area*2.5

span = (aspect_ratio*ref_area)**0.5
root_chord = 2*ref_area/span*(1+taper_ratio)

tip_chord = root_chord*taper_ratio

mac = root_chord*2.0*(1 + taper_ratio + taper_ratio**2)/(3.0*(1+taper_ratio))

print 'Root Chord', root_chord
print 'Tip chord', tip_chord
print 'span', span
print 'AR', aspect_ratio
print 'Wetted area', wetted_area
print 'MAC', mac
print 'Geometric mean chord', (root_chord+tip_chord)/2


