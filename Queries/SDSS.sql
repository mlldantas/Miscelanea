SELECT res.Objid, res.plate, res.mjd, res.fiberid, res.ra, res.dec, g.modelMag_u, g.modelMag_g, g.modelMag_r, g.modelMag_i, g.modelMag_z, res.fuv_mag, res.nuv_mag, g.dered_u, g.dered_g, g.dered_r, g.dered_i, g.dered_z, g.petroR90_r, res.fuv_magerr, res.nuv_magerr, g.fiberMag_z, res.e_bv, s.sn_1 as s2n_r, res.sn_fuv_auto, res.survey, g.type
INTO MyDB.SDSS_results_01
FROM MyDB.Galex_results_01 AS res, Galaxy AS g, SpecObj AS s
WHERE g.nchild = 0 AND (g.Flags & (0x0000000000040000 + 0x0000000000000002 + 0x0000080000000000) ) = 0 AND g.dered_r<=22.0 AND (g.dered_u between 5 AND 30) AND (g.dered_g between 5 AND 30) AND g.dered_r > 5 AND (g.dered_i between 5 AND 30) AND (g.dered_z between 5 AND 30) AND s.specClass = 2 AND s.zStatus > 1 AND s.zConf > 0.9 AND s.zWarning = 0 AND res.Objid = g.objid AND g.objid = s.bestObjID AND s.z BETWEEN 0.05 AND 0.075 AND (g.petroR90_r BETWEEN 1.5 AND 3.5)
ORDER BY res.plate, res.mjd, res.fiberid

/*specClass = 2 are galaxies spectra*/
/*nchild = 0 - Number of children if this is a composite object that has been deblended. BRIGHT (in a flags sense) objects also have nchild == 1, the non-BRIGHT sibling.*/
/*0x0000000000040000 - Object contains one or more saturated pixels*/
/*0x0000000000000002 - Object detected in first, bright object-finding; generally r*<17.5*/
/*0x0000080000000000 - Object center is close to at least one saturated pixel.*/
/*zWarning = 0 - Spectra with zWarning equal to zero have no known problems. */
/*zConf*/
