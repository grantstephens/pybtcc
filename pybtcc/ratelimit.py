import time
import logging

log = logging.getLogger(__name__)


def RateLimiter(f):
    burstCount = [0]
    firstBurst = [0.0]

    def wrapper(*args, **kwargs):
        maxPerSecond = args[0].maxRate
        burst = args[0].maxBurst
        minInterval = 1.0 / float(maxPerSecond)
        if burstCount[0] == 0:
            firstBurst[0] = time.time()
        if burstCount[0] < burst:
            burstCount[0] += 1
            ret = f(*args, **kwargs)
        if burstCount[0] == burst:
            burstCount[0] = 0
            elapsed = time.time() - firstBurst[0]
            leftToWait = + burst*minInterval - elapsed
            if leftToWait > 0:
                log.warning('Rate limited! Waiting {:.2f}s'.format(leftToWait))
                time.sleep(leftToWait)
        return ret
    return wrapper
