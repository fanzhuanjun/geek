```python
import pandas as pd
```


```python
pew = pd.read_csv('../data/pew.csv')
```


```python
pew.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>religion</th>
      <th>&lt;$10k</th>
      <th>$10-20k</th>
      <th>$20-30k</th>
      <th>$30-40k</th>
      <th>$40-50k</th>
      <th>$50-75k</th>
      <th>$75-100k</th>
      <th>$100-150k</th>
      <th>&gt;150k</th>
      <th>Don't know/refused</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Agnostic</td>
      <td>27</td>
      <td>34</td>
      <td>60</td>
      <td>81</td>
      <td>76</td>
      <td>137</td>
      <td>122</td>
      <td>109</td>
      <td>84</td>
      <td>96</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Atheist</td>
      <td>12</td>
      <td>27</td>
      <td>37</td>
      <td>52</td>
      <td>35</td>
      <td>70</td>
      <td>73</td>
      <td>59</td>
      <td>74</td>
      <td>76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Buddhist</td>
      <td>27</td>
      <td>21</td>
      <td>30</td>
      <td>34</td>
      <td>33</td>
      <td>58</td>
      <td>62</td>
      <td>39</td>
      <td>53</td>
      <td>54</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Catholic</td>
      <td>418</td>
      <td>617</td>
      <td>732</td>
      <td>670</td>
      <td>638</td>
      <td>1116</td>
      <td>949</td>
      <td>792</td>
      <td>633</td>
      <td>1489</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Don’t know/refused</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
      <td>11</td>
      <td>10</td>
      <td>35</td>
      <td>21</td>
      <td>17</td>
      <td>18</td>
      <td>116</td>
    </tr>
  </tbody>
</table>
</div>




```python
pew_long = pd.melt(pew, id_vars='religion')
```


```python
pew_long
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>religion</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Agnostic</td>
      <td>&lt;$10k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Atheist</td>
      <td>&lt;$10k</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Buddhist</td>
      <td>&lt;$10k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Catholic</td>
      <td>&lt;$10k</td>
      <td>418</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Don’t know/refused</td>
      <td>&lt;$10k</td>
      <td>15</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Evangelical Prot</td>
      <td>&lt;$10k</td>
      <td>575</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Hindu</td>
      <td>&lt;$10k</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Historically Black Prot</td>
      <td>&lt;$10k</td>
      <td>228</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Jehovah's Witness</td>
      <td>&lt;$10k</td>
      <td>20</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Jewish</td>
      <td>&lt;$10k</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Mainline Prot</td>
      <td>&lt;$10k</td>
      <td>289</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Mormon</td>
      <td>&lt;$10k</td>
      <td>29</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Muslim</td>
      <td>&lt;$10k</td>
      <td>6</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Orthodox</td>
      <td>&lt;$10k</td>
      <td>13</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Other Christian</td>
      <td>&lt;$10k</td>
      <td>9</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Other Faiths</td>
      <td>&lt;$10k</td>
      <td>20</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Other World Religions</td>
      <td>&lt;$10k</td>
      <td>5</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Unaffiliated</td>
      <td>&lt;$10k</td>
      <td>217</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Agnostic</td>
      <td>$10-20k</td>
      <td>34</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Atheist</td>
      <td>$10-20k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Buddhist</td>
      <td>$10-20k</td>
      <td>21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Catholic</td>
      <td>$10-20k</td>
      <td>617</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Don’t know/refused</td>
      <td>$10-20k</td>
      <td>14</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Evangelical Prot</td>
      <td>$10-20k</td>
      <td>869</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Hindu</td>
      <td>$10-20k</td>
      <td>9</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Historically Black Prot</td>
      <td>$10-20k</td>
      <td>244</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Jehovah's Witness</td>
      <td>$10-20k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Jewish</td>
      <td>$10-20k</td>
      <td>19</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Mainline Prot</td>
      <td>$10-20k</td>
      <td>495</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Mormon</td>
      <td>$10-20k</td>
      <td>40</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>150</th>
      <td>Hindu</td>
      <td>&gt;150k</td>
      <td>54</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Historically Black Prot</td>
      <td>&gt;150k</td>
      <td>78</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Jehovah's Witness</td>
      <td>&gt;150k</td>
      <td>6</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Jewish</td>
      <td>&gt;150k</td>
      <td>151</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Mainline Prot</td>
      <td>&gt;150k</td>
      <td>634</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Mormon</td>
      <td>&gt;150k</td>
      <td>42</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Muslim</td>
      <td>&gt;150k</td>
      <td>6</td>
    </tr>
    <tr>
      <th>157</th>
      <td>Orthodox</td>
      <td>&gt;150k</td>
      <td>46</td>
    </tr>
    <tr>
      <th>158</th>
      <td>Other Christian</td>
      <td>&gt;150k</td>
      <td>12</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Other Faiths</td>
      <td>&gt;150k</td>
      <td>41</td>
    </tr>
    <tr>
      <th>160</th>
      <td>Other World Religions</td>
      <td>&gt;150k</td>
      <td>4</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Unaffiliated</td>
      <td>&gt;150k</td>
      <td>258</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Agnostic</td>
      <td>Don't know/refused</td>
      <td>96</td>
    </tr>
    <tr>
      <th>163</th>
      <td>Atheist</td>
      <td>Don't know/refused</td>
      <td>76</td>
    </tr>
    <tr>
      <th>164</th>
      <td>Buddhist</td>
      <td>Don't know/refused</td>
      <td>54</td>
    </tr>
    <tr>
      <th>165</th>
      <td>Catholic</td>
      <td>Don't know/refused</td>
      <td>1489</td>
    </tr>
    <tr>
      <th>166</th>
      <td>Don’t know/refused</td>
      <td>Don't know/refused</td>
      <td>116</td>
    </tr>
    <tr>
      <th>167</th>
      <td>Evangelical Prot</td>
      <td>Don't know/refused</td>
      <td>1529</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Hindu</td>
      <td>Don't know/refused</td>
      <td>37</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Historically Black Prot</td>
      <td>Don't know/refused</td>
      <td>339</td>
    </tr>
    <tr>
      <th>170</th>
      <td>Jehovah's Witness</td>
      <td>Don't know/refused</td>
      <td>37</td>
    </tr>
    <tr>
      <th>171</th>
      <td>Jewish</td>
      <td>Don't know/refused</td>
      <td>162</td>
    </tr>
    <tr>
      <th>172</th>
      <td>Mainline Prot</td>
      <td>Don't know/refused</td>
      <td>1328</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Mormon</td>
      <td>Don't know/refused</td>
      <td>69</td>
    </tr>
    <tr>
      <th>174</th>
      <td>Muslim</td>
      <td>Don't know/refused</td>
      <td>22</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Orthodox</td>
      <td>Don't know/refused</td>
      <td>73</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Other Christian</td>
      <td>Don't know/refused</td>
      <td>18</td>
    </tr>
    <tr>
      <th>177</th>
      <td>Other Faiths</td>
      <td>Don't know/refused</td>
      <td>71</td>
    </tr>
    <tr>
      <th>178</th>
      <td>Other World Religions</td>
      <td>Don't know/refused</td>
      <td>8</td>
    </tr>
    <tr>
      <th>179</th>
      <td>Unaffiliated</td>
      <td>Don't know/refused</td>
      <td>597</td>
    </tr>
  </tbody>
</table>
<p>180 rows × 3 columns</p>
</div>




```python
pew_long = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
pew_long.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>religion</th>
      <th>income</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Agnostic</td>
      <td>&lt;$10k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Atheist</td>
      <td>&lt;$10k</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Buddhist</td>
      <td>&lt;$10k</td>
      <td>27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Catholic</td>
      <td>&lt;$10k</td>
      <td>418</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Don’t know/refused</td>
      <td>&lt;$10k</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard = pd.read_csv('../data/billboard.csv')
```


```python
billboard.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>wk1</th>
      <th>wk2</th>
      <th>wk3</th>
      <th>wk4</th>
      <th>wk5</th>
      <th>...</th>
      <th>wk67</th>
      <th>wk68</th>
      <th>wk69</th>
      <th>wk70</th>
      <th>wk71</th>
      <th>wk72</th>
      <th>wk73</th>
      <th>wk74</th>
      <th>wk75</th>
      <th>wk76</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>87</td>
      <td>82.0</td>
      <td>72.0</td>
      <td>77.0</td>
      <td>87.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>2000-09-02</td>
      <td>91</td>
      <td>87.0</td>
      <td>92.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2000-04-08</td>
      <td>81</td>
      <td>70.0</td>
      <td>68.0</td>
      <td>67.0</td>
      <td>66.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>76</td>
      <td>76.0</td>
      <td>72.0</td>
      <td>69.0</td>
      <td>67.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>2000-04-15</td>
      <td>57</td>
      <td>34.0</td>
      <td>25.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 81 columns</p>
</div>




```python
billboard_long = pd.melt(
    billboard,
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='week',
    value_name='rating'
)
```


```python
billboard_long.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>2000-09-02</td>
      <td>wk1</td>
      <td>91.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2000-04-08</td>
      <td>wk1</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk1</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>2000-04-15</td>
      <td>wk1</td>
      <td>57.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard_long.shape
```




    (24092, 7)




```python
ebola = pd.read_csv('../data/country_timeseries.csv')
```


```python
ebola.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>Cases_Guinea</th>
      <th>Cases_Liberia</th>
      <th>Cases_SierraLeone</th>
      <th>Cases_Nigeria</th>
      <th>Cases_Senegal</th>
      <th>Cases_UnitedStates</th>
      <th>Cases_Spain</th>
      <th>Cases_Mali</th>
      <th>Deaths_Guinea</th>
      <th>Deaths_Liberia</th>
      <th>Deaths_SierraLeone</th>
      <th>Deaths_Nigeria</th>
      <th>Deaths_Senegal</th>
      <th>Deaths_UnitedStates</th>
      <th>Deaths_Spain</th>
      <th>Deaths_Mali</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>2776.0</td>
      <td>NaN</td>
      <td>10030.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1786.0</td>
      <td>NaN</td>
      <td>2977.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>2775.0</td>
      <td>NaN</td>
      <td>9780.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1781.0</td>
      <td>NaN</td>
      <td>2943.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>2769.0</td>
      <td>8166.0</td>
      <td>9722.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1767.0</td>
      <td>3496.0</td>
      <td>2915.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>NaN</td>
      <td>8157.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3496.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>2730.0</td>
      <td>8115.0</td>
      <td>9633.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1739.0</td>
      <td>3471.0</td>
      <td>2827.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
ebola_long.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>Cases_Guinea</td>
      <td>2776.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>Cases_Guinea</td>
      <td>2775.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>Cases_Guinea</td>
      <td>2769.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>Cases_Guinea</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>Cases_Guinea</td>
      <td>2730.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
'Cases_Guinea'.split('_')
```




    ['Cases', 'Guinea']




```python
# string accessor
variable_split = ebola_long['variable'].str.split('_')
```


```python
type(variable_split)
```




    pandas.core.series.Series




```python
variable_split.head()
```




    0    [Cases, Guinea]
    1    [Cases, Guinea]
    2    [Cases, Guinea]
    3    [Cases, Guinea]
    4    [Cases, Guinea]
    Name: variable, dtype: object




```python
type(variable_split[0])
```




    list




```python
variable_split[0][1]
```




    'Guinea'




```python
status_values = variable_split.str.get(0)
status_values.head()
```




    0    Cases
    1    Cases
    2    Cases
    3    Cases
    4    Cases
    Name: variable, dtype: object




```python
country_values = variable_split.str.get(1)
country_values.head()
```




    0    Guinea
    1    Guinea
    2    Guinea
    3    Guinea
    4    Guinea
    Name: variable, dtype: object




```python
ebola_long['status'] = status_values
ebola_long['country'] = country_values
```


```python
ebola_long.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>variable</th>
      <th>value</th>
      <th>status</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>Cases_Guinea</td>
      <td>2776.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>Cases_Guinea</td>
      <td>2775.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>Cases_Guinea</td>
      <td>2769.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>Cases_Guinea</td>
      <td>NaN</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>Cases_Guinea</td>
      <td>2730.0</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
  </tbody>
</table>
</div>




```python
variable_split = ebola_long['variable'].str.split('_', expand=True)
```


```python
type(variable_split)
```




    pandas.core.frame.DataFrame




```python
variable_split.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
  </tbody>
</table>
</div>




```python
variable_split.columns = ['status_expand', 'country_expand']
```


```python
variable_split.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>status_expand</th>
      <th>country_expand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
  </tbody>
</table>
</div>




```python
ebola_long = pd.concat([ebola_long, variable_split], axis=1)
```


```python
ebola_long.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Day</th>
      <th>variable</th>
      <th>value</th>
      <th>status</th>
      <th>country</th>
      <th>status_expand</th>
      <th>country_expand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/5/2015</td>
      <td>289</td>
      <td>Cases_Guinea</td>
      <td>2776.0</td>
      <td>Cases</td>
      <td>Guinea</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/4/2015</td>
      <td>288</td>
      <td>Cases_Guinea</td>
      <td>2775.0</td>
      <td>Cases</td>
      <td>Guinea</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2015</td>
      <td>287</td>
      <td>Cases_Guinea</td>
      <td>2769.0</td>
      <td>Cases</td>
      <td>Guinea</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/2/2015</td>
      <td>286</td>
      <td>Cases_Guinea</td>
      <td>NaN</td>
      <td>Cases</td>
      <td>Guinea</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/31/2014</td>
      <td>284</td>
      <td>Cases_Guinea</td>
      <td>2730.0</td>
      <td>Cases</td>
      <td>Guinea</td>
      <td>Cases</td>
      <td>Guinea</td>
    </tr>
  </tbody>
</table>
</div>




```python
weather = pd.read_csv('../data/weather.csv')
```


```python
weather.shape
```




    (22, 35)




```python
weather.iloc[:5, :11]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>element</th>
      <th>d1</th>
      <th>d2</th>
      <th>d3</th>
      <th>d4</th>
      <th>d5</th>
      <th>d6</th>
      <th>d7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>27.3</td>
      <td>24.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmin</td>
      <td>NaN</td>
      <td>14.4</td>
      <td>14.4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>tmax</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
weather_melt = pd.melt(
    weather,
    id_vars=['id', 'year', 'month', 'element'],
    var_name='day',
    value_name='temp'
)
```


```python
weather_melt.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>element</th>
      <th>day</th>
      <th>temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmax</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>tmin</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmax</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>2</td>
      <td>tmin</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>3</td>
      <td>tmax</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
weather_tidy = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'day'],
    columns='element',
    values='temp'
)
```


```python
type(weather_tidy)
```




    pandas.core.frame.DataFrame




```python
weather_tidy.reset_index().head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>element</th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>tmax</th>
      <th>tmin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d10</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d11</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d13</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
weather_tidy = (weather_melt
                .pivot_table(
                    index=['id', 'year', 'month', 'day'],
                    columns='element',
                    values='temp')
                .reset_index()
)
```


```python
weather_tidy.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>element</th>
      <th>id</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>tmax</th>
      <th>tmin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d10</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d11</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MX17004</td>
      <td>2010</td>
      <td>1</td>
      <td>d13</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard_long.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>2000-09-02</td>
      <td>wk1</td>
      <td>91.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2000-04-08</td>
      <td>wk1</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk1</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>2000-04-15</td>
      <td>wk1</td>
      <td>57.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard_long[billboard_long['track'] == 'Loser']
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk1</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>320</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk2</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>637</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk3</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>954</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk4</td>
      <td>69.0</td>
    </tr>
    <tr>
      <th>1271</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk5</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>1588</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk6</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>1905</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk7</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>2222</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk8</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>2539</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk9</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>2856</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk10</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>3173</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk11</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>3490</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk12</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>3807</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk13</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>4124</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk14</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>4441</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk15</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>4758</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk16</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>5075</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk17</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>5392</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk18</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>5709</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk19</td>
      <td>73.0</td>
    </tr>
    <tr>
      <th>6026</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk20</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>6343</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk21</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6660</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk22</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6977</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk23</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7294</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk24</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7611</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk25</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7928</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk26</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8245</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk27</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8562</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk28</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8879</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk29</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9196</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk30</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>14585</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk47</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14902</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk48</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15219</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk49</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15536</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk50</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15853</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk51</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16170</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk52</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16487</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk53</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16804</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk54</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17121</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk55</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17438</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk56</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17755</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk57</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18072</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk58</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18389</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk59</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18706</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk60</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19023</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk61</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19340</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk62</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19657</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk63</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19974</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk64</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20291</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk65</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20608</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk66</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20925</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk67</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21242</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk68</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21559</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk69</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21876</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk70</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22193</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk71</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22510</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk72</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22827</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk73</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23144</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk74</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23461</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk75</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23778</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>2000-10-21</td>
      <td>wk76</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>76 rows × 7 columns</p>
</div>




```python
billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
```


```python
billboard_songs.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard_songs.shape
```




    (24092, 4)




```python
billboard_songs = billboard_songs.drop_duplicates()
```


```python
billboard_songs.shape
```




    (317, 4)




```python
range(10)
```




    range(0, 10)




```python
billboard_songs.shape[0]
```




    317




```python
len(billboard_songs)
```




    317




```python
billboard_songs['id'] = range(len(billboard_songs))
```


```python
billboard_songs.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2Ge+her</td>
      <td>The Hardest Part Of ...</td>
      <td>3:15</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Kryptonite</td>
      <td>3:53</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>3 Doors Down</td>
      <td>Loser</td>
      <td>4:24</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>504 Boyz</td>
      <td>Wobble Wobble</td>
      <td>3:35</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2000</td>
      <td>98^0</td>
      <td>Give Me Just One Nig...</td>
      <td>3:24</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2000</td>
      <td>A*Teens</td>
      <td>Dancing Queen</td>
      <td>3:44</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2000</td>
      <td>Aaliyah</td>
      <td>I Don't Wanna</td>
      <td>4:15</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2000</td>
      <td>Aaliyah</td>
      <td>Try Again</td>
      <td>4:03</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2000</td>
      <td>Adams, Yolanda</td>
      <td>Open My Heart</td>
      <td>5:30</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard_ratings = billboard_long.merge(
    billboard_songs, on=['year', 'artist', 'track', 'time']
)
```


```python
billboard_ratings.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk2</td>
      <td>82.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk3</td>
      <td>72.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk4</td>
      <td>77.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>2 Pac</td>
      <td>Baby Don't Cry (Keep...</td>
      <td>4:22</td>
      <td>2000-02-26</td>
      <td>wk5</td>
      <td>87.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
billboard_ratings = billboard_ratings[['id', 'date.entered', 'week', 'rating']]
```


```python
billboard_ratings.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>date.entered</th>
      <th>week</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk1</td>
      <td>87.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk2</td>
      <td>82.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk3</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk4</td>
      <td>77.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>2000-02-26</td>
      <td>wk5</td>
      <td>87.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
