import Bench.TS_datasets as tsds
import tests.artificial.process_artificial_dataset as art




dataset = tsds.generate_random_TS(N = 32 , FREQ = 'D', seed = 0, trendtype = "poly", cycle_length = 0, transform = "diff", sigma = 0.0, exog_count = 20);

art.process_dataset(dataset);