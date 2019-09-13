from __future__ import division
import pydoop.hdfs as hdfs
import pydoop.mapreduce.api as api
import pydoop.mapreduce.pipes as pp

class Mapper(api.Mapper):
    def map(self,context):
        lines=context.value.split(",");
        origin_apt=lines[16]
        dep_delay=lines[15]
        if(dep_delay!='DepDelay'):
            if(dep_delay!='NA'):
                if(int(dep_delay)>0):
                    context.emit(origin_apt,1)
                else:
                    context.emit(origin_apt,0)
            else:
                context.emit(origin_apt,0)

class Reducer(api.Reducer):
    def reduce(self,context):
        total_entries=[]
        delay_entries=[]
        for value in context.values:
            total_entries.append(value)
            if(value==1):
                delay_entries.append(value)
        context.emit(context.key,len(delay_entries)/len(total_entries)*100)

def __main__():
    pp.run_task(pp.Factory(Mapper,Reducer))