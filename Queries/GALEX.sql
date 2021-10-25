SELECT r.Objid, r.plate, r.mjd, r.fiberid, p.ra, p.dec, p.nuv_mag, p.fuv_mag, p.nuv_magerr, p.fuv_magerr, p.e_bv, p.fuv_s2n as sn_fuv_auto, pe.mpstype as survey 
INTO mydb.Galex_results_01
FROM PhotoObjAll as p, XSDSSDR7 as s, MyDB.starlight_params as r, photoextract as pe
WHERE (p.objid = s.objid AND s.SDSSObjid = r.ObjID AND pe.photoExtractID = p.photoExtractID AND p.nuv_mag > -99 AND (p.fuv_mag > -99 AND p.fuv_mag < 19) AND p.band=3 AND s.multipleMatchCount = 1 )
ORDER BY r.plate, r.mjd, r.fiberid

/*band = 3 - objects that have both fuv and nuv measurements*/
/*multipleMatchCount = 1 - an integer, for any given GALEX object how many SDSS objects it matched, for example a value of 1 indicates the GALEX object only matched 1 SDSS object within the 5" match radius.*/
/*fuv_s2n - FUV signal-to-noise from 'AUTO' flux value - This is the ratio of FUV_FLUX_AUTO and FUV_FLUXERR_AUTO.*/
