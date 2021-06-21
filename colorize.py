import numpy as np
import cv2 as cv
def image_colorization(image_file):
        W_in = 224
        H_in = 224
        imshowSize = (640, 480)
        net = cv.dnn.readNetFromCaffe("models/colorization_deploy_v2.prototxt", "models/colorization_release_v2.caffemodel")
        pts_in_hull = np.load("models/pts_in_hull.npy") 
        pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1)
        net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull.astype(np.float32)]
        net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]
        frame=cv.imread("static/origin/"+image_file)
        frame= frame[:,:,[2, 1, 0]]
        img_rgb = ( frame * 1.0 / 255).astype(np.float32)
        img_lab = cv.cvtColor(img_rgb, cv.COLOR_RGB2Lab)
        img_l = img_lab[:,:,0]
        (H_orig,W_orig) = img_rgb.shape[:2]
        img_rs = cv.resize(img_rgb, (W_in, H_in)) 
        img_lab_rs = cv.cvtColor(img_rs, cv.COLOR_RGB2Lab)
        img_l_rs = img_lab_rs[:,:,0]
        img_l_rs -= 50 
        net.setInput(cv.dnn.blobFromImage(img_l_rs))
        ab_dec = net.forward('class8_ab')[0,:,:,:].transpose((1,2,0)) 
        (H_out,W_out) = ab_dec.shape[:2]
        ab_dec_us = cv.resize(ab_dec, (W_orig, H_orig))
        img_lab_out = np.concatenate((img_l[:,:,np.newaxis],ab_dec_us),axis=2) 
        img_bgr_out = cv.cvtColor(img_lab_out, cv.COLOR_Lab2BGR)
        img_bgr_out = 255 * np.clip(img_bgr_out, 0, 1)
        img_bgr_out = np.uint8(img_bgr_out)
        cv.imwrite('static/out/'+image_file,img_bgr_out)