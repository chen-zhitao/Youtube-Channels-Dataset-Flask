# Flask API for Youtube Channels Dataset

This repository contains the source code for deploying the dataset from <https://github.com/chen-zhitao/Youtube-Channels-Dataset>.

You can test querying data from the dataset on <https://youtube-channels-dataset.onrender.com>.
The result will be in JSON.

## Technical notes
* The full dataset is split into two .db files under /data for convienet upload to Github.
* When a user tries querying from a Youtube channel url, we visits the url and parse the HTML to retrieve the channelId, which is then used to query entries from the dataset. The reason is that a user may enter a url containing the Youtube channel handle, like https://www.youtube.com/@veritasium. In this case, veritasium is in our dataset, but under a different url which contains its channel Id.

## Personal notes
* Some of my other favorite channels are in the dataset, like @TeamCoco, @JJRedick, @HasanMinhaj. But some other smaller channels like @kofuzi or bigger channels with niche topics like @TheCottageFairy are not. Youtube has 30K+ channels with 1M+ subscribers, so not all of our favorite channels are covered in this dataset of 16K+ channels.
