FROM emanaev/redshift3d

RUN wget -q https://s3.amazonaws.com/s3.redshift3d.com/public/benchmark/RedshiftBenchmarkScenes.tar.gz && \
  tar -xvf RedshiftBenchmarkScenes.tar.gz && \
  rm RedshiftBenchmarkScenes.tar.gz

RUN chmod +x ./runBenchmark.sh
CMD ["./runBenchmark.sh"]
