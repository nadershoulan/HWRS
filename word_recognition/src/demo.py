from path import Path
import os
if __name__ == '__main__':
    data_dir= r'C:\Users\nadershoulan\Desktop\MyWork\Universtiy\Final project\repo\Arabic Hand Writing Recognition System\word_recognition\data'
    root_img='../data/img/'
    root_txt = '../data/gt/'
    print(data_dir+'/word_list/words.txt')
    f = open(data_dir +'/word_list/words.txt')

    # filenames_img = sorted(os.listdir(root_img))
    filenames_gt = sorted(os.listdir(root_txt))
    # filenames_imgsplit = [filename.replace('.jpg', '') for filename in filenames_img]
    # filenames_gtsplit = [filename.replace('.txt', '') for filename in filenames_gt]
    # print(filenames_img[4])
    print((filenames_gt))

    # chars = set()
    # # bad_samples_reference = ['a01-117-05-02', 'r06-022-03-05']  # known broken images in IAM dataset
    for line in filenames_gt:
    #     # ignore empty and comment lines
        line = line.strip()
        if not line :
            continue
        file_name = data_dir + '\\img\\' + line.replace('.txt', '.jpg')
        # print(file_name)
    #
    #     # # GT text are columns starting at 9
        f = open(root_txt + '/'+line, encoding="utf8")
        chars = set()
        gt_text = ' '.join(f)
        print(gt_text)
