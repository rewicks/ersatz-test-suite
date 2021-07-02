# Test Suites

Within the segmented folder, you will find available test suites for a variety of languages. These test sets are derived mostly from WMT news translation test sets and were manually resegmented in order to test sentence segmentation performance.

For more information, please see: 

- [Rachel Wicks and Matt Post (2021) :
   A unified approach to sentence segmentation of punctuated text in many languages]() In _Proceedings of ACL_.

The scores reported in the above paper were tested on sentences with punctuated contexts. Sentences without sentence-final punctuation were removed with the `punc-stripper.py` script. To recreate scores, the following sequence of commands can be used:

```angular2html
cat segmented/en/wsj.03-06.en | punc_stripper.py > test.en
cat test.en | tr '\n' ' ' | ersatz -m en > segmented
ersatz_score test segmented

```

# Errors in Segmentation

If you find errors in these segmentations, please submit a pull request and we can correct them if they seem reasonable.

# Known issues

There is some question on whether we should segment in embedded quotes. Consider the following:

```angular2html
He says the big questions -- "Do you really need this much money to put up these investments? Have you told investors what is happening in your sector? What about your track record? -- "aren't asked of companies coming to market.
```

As you can see, there are many sentences embedded within a quote. The overall sentence is wrapped around this quote. In this case, we find it reasonable to not segment though most segmentation systems will segment here.

We do, however, segment in the following circumstance:

```angular2html
"We have to achieve the free movement of citizens and workers for any South American country, as is already the situation with members of the Andean Community.
However, there are still reactionary sectors that want us to return to the past" he said.
```

when there is not a lexical wrapping around the quote (notice it is only the initial quotation that is broken apart here).

There is also often sentence fragments that are punctuated as a full sentence. Consider:

```angular2html
I'll see you Wednesday?... Thursday."
```
or
```angular2html
Wham! Bam!
```

In this case, we often keep this fragment unsegmented, though an easy argument can be made to segment.

