SELECT e.*, s.z AS redshift, s.modelMag_u, s.modelMag_g, s.modelMag_r, s.modelMag_i, s.modelMag_z, s.dered_u, s.dered_g, s.dered_r, s.dered_i, s.dered_z, g.petroR50_r
FROM MyDB.example AS e, SpecPhotoAll AS s, PhotoObjAll as g
WHERE (g.ObjID = e.objID) AND (s.ObjID = e.objID)
INTO MyDB.teste03
