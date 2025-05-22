SELECT e.*, s.z AS redshift, s.modelMag_u, s.modelMag_g, s.modelMag_r, s.modelMag_i, s.modelMag_z, s.dered_u, s.dered_g, s.dered_r, s.dered_i, s.dered_z
FROM MyDB.example AS e, SpecPhotoAll AS s
WHERE (e.plate = s.plate) AND (e.mjd = s.mjd) AND (e.fiberID = s.fiberID)
INTO MyDB.teste02
