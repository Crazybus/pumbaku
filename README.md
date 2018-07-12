# PUMBAKU

Pumbaku tries his best to validate Haiku messages in your dedicated Haiku slack channel. Our channel is called #haikunamatata. 

![PUMBAKU](https://i.imgur.com/Bo7lwMcm.png)

## Examples

Pumbaku isn't the smartest but he tries his best.

```
Michael Russell [06:48]
what-love-is

Pumbaku APP [06:48]
PUMBAKU DO NOT KNOW WHAT-LOVE-IS
```

```
crazybus [21:26]
joined #haikunamatata.

Pumbaku APP [21:26]
PUMBAKU DO NOT KNOW @CRAZYBUS
```

```
Michael Russell [20:27]
An old silent pond. A frog jumps into the pond. Splash silence again again

Pumbaku APP [20:27]
HAS 19 SYLLABLES! IS NOT HAIKU!
```

He gets excited if you do get it right though!

```
Michael Russell [20:27]
An old silent pond. A frog jumps into the pond. Splash silence again

Pumbaku APP [20:27]
AN OLD SILENT POND
A FROG JUMPS INTO THE POND
SPLASH SILENCE AGAIN
```

## Running

* Get a [slack legacy token](https://api.slack.com/custom-integrations/legacy-tokens) and set it to `SLACK_BOT_TOKEN`
* Set `HAIKU_CHANNEL` to the channel id you want to use

```
$ export SLACK_BOT_TOKEN='xoxp-231234234234234234234234234`
$ HAIKU_CHANNEL=C8M579BNU make run
```

## Testing

```
$ make test
```

## Debugging

```
$ make debug
message: test
checking for haiku in: "test"
HAS 1 SYLLABLES! IS NOT HAIKU!
```


## Why is he shouting?

The bot is based on  [python-haikubot](https://github.com/tlastowka/python-haikubot). Internally this bot was using a list of words with syllables which are stored in uppercase for some reason. I wanted to modify the bot to print the haiku with the 5/7/5 structure with newlines. When I did this it used the uppercased words which was hilarious so I kept it like that. 
