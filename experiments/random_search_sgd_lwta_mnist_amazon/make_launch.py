base = """jobdispatch --torque --env=THEANO_FLAGS=device=gpu,floatX=float32,force_device=True --duree=24:00:00 --whitespace --gpu $F/experiments/random_search_dropout_lwta_mnist/worker.sh $F/experiments/random_search_dropout_lwta_mnist/exp/"{{%(args)s}}\""""
args = ','.join([str(job_id) for job_id in xrange(25)])
f = open('launch.sh', 'w')
f.write(base % locals())
f.close()
