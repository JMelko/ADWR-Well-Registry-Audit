CREATE TABLE pima_wells_production AS
SELECT DISTINCT ON (registry_id) 
    registry_id, 
    owner_name, 
    well_type, 
    well_depth, 
    x, 
    y
FROM pima_wells
ORDER BY registry_id, well_depth DESC;